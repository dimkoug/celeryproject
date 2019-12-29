from celery import shared_task
import time


@shared_task(bind=True)
def my_task(self, items):
    result = {}
    counter = 0
    for index, value in enumerate(items):
        time.sleep(1)
        counter += value
        if not self.request.called_directly:
            self.update_state(state='PROGRESS',
                meta={'current': index+1, 'total': len(items)})
    result['counter'] = counter
    return result

