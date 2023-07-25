from celery_tasks.send_msg import send_msg
from celery_tasks.send_email import send_email

result = send_email.delay('test1')
print(result.id)
result = send_msg.delay('test2')
print(result.id)
