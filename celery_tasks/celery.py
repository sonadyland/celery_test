
import celery
import time

from kombu import Queue


queues_learning = 'https://www.jianshu.com/p/4d0bbdbc6ade'
backend = 'redis://:123456@127.0.0.1:6379/3'
broker = 'redis://:123456@127.0.0.1:6379/4'
cel = celery.Celery('test', backend=backend, broker=broker)

cel = celery.Celery(
    'test',
    broker=broker,
    backend=backend,
    include=['celery_tasks.send_email',
             'celery_tasks.send_msg'
             ]
)

celery_queues = (
    Queue('default', routing_key='default'),
    Queue('email', routing_key='email'),
    Queue('msg', routing_key='msg'),
)

celery_routes = {
    'celery_tasks.send_email.send_email': {'queue': 'email', 'routing_key': 'email'},
    'celery_tasks.send_msg.send_msg': {'queue': 'msg', 'routing_key': 'msg'},
}

cel.conf.beat_schedule = {
    'send_email': {
        'task': 'celery_tasks.send_email.send_email',
        'schedule': 10.0,
        'args': ('0.1 times/s',)
    },
    'send_msg': {
        'task': 'celery_tasks.send_msg.send_msg',
        'schedule': 5.0,
        'args': ('0.2 times/s',)
    }
}
