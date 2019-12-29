Django project application with celery , channels , basic project 
-----------


Quick start
-----------

1. Clone repo  like this::

     git clone  https://github.com/dimkoug/celeryproject.git

2. Create a virtualenv::

     python3 -m venv virtualenv

3. Activate virtualenv

4. Install packages from requirements.txt file


5. inside /etc/hosts create an entry  127.0.0.1 celeryproject

6. inside deploy folder there are the conf  sample  files , change paths according to your configuration

7. in  linux install supervisor and nginx::
    
     apt-get install supervisor nginx

8. Create symlinks of conf files::
    
     sudo ln -sf  /path/to/celeryproject/deploy/conf/nginx.conf /etc/nginx/sites-enabled/celeryproject.conf
     sudo ln -sf  /path/to/celeryproject/deploy/conf/gunicorn.conf /etc/supervisor/conf.d/celeryproject.conf
     sudo ln -sf  /path/to/celeryproject/deploy/conf/celery_beat.conf /etc/supervisor/conf.d/celeryproject_celery_beat.conf
     sudo ln -sf  /path/to/celeryproject/deploy/conf/celery_worker.conf /etc/supervisor/conf.d/celeryproject_celery_worker.conf
     sudo ln -sf  /path/to/celeryproject/deploy/conf/daphne.conf /etc/supervisor/conf.d/celeryproject_daphne.conf
     sudo supervisorctl reread
     sudo supervisorctl update
     sudo supervisorctl start celeryproject


9. For celery async task :  http://celeryproject/

10. For chat application : http://celeryproject/chat/
