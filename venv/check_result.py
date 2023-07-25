from celery.result import AsyncResult
from celery_tasks.celery import cel

async_result = AsyncResult(id='c6c25a55-79de-4c95-adb4-309bcdde216f', app=cel)

if async_result.successful():
    result = async_result.get()
    print('success', result)
