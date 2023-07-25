import time
from celery_tasks.celery import cel


@cel.task
def send_email(name):
    print('send msg %s'%name)
    return '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'