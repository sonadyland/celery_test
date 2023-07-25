import time

from celery_tasks.celery import cel


@cel.task
def send_msg(name):
    print('send email %s' % name)
    return '##############################################'
