sudo ln -sf  /path/to/celeryproject/deploy/conf/nginx.conf /etc/nginx/sites-enabled/celeryproject.conf

sudo ln -sf  /path/to/celeryproject/deploy/conf/gunicorn.conf /etc/supervisor/conf.d/celeryproject.conf

sudo ln -sf  /path/to/celeryproject/deploy/conf/celery_beat.conf /etc/supervisor/conf.d/celeryproject_celery_beat.conf

sudo ln -sf  /path/to/celeryproject/deploy/conf/celery_worker.conf /etc/supervisor/conf.d/celeryproject_celery_worker.conf

sudo ln -sf  /path/to/celeryproject/deploy/conf/daphne.conf /etc/supervisor/conf.d/celeryproject_daphne.conf

sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start celeryproject
