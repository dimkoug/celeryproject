import json
import datetime
from django.http import JsonResponse
from django.views.generic import TemplateView
from celery.result import AsyncResult
from .tasks import my_task

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = [i+1 for i in range(0, 10)]
        result = my_task.apply_async(args=[items], eta=datetime.datetime.now())
        task_id = result.task_id
        context['task_id'] = task_id
        context['items_len'] = len(items)
        return context

def get_progress(request, task_id):
    result = AsyncResult(task_id)
    response_data = {
        'state': result.state,
        'details': result.info,
    }
    return JsonResponse(response_data)
