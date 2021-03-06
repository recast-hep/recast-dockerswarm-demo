import os
CELERY_RESULT_BACKEND = "redis"
CELERY_REDIS_HOST = os.environ['REDIS_PORT_6379_TCP_ADDR']
CELERY_REDIS_PORT = os.environ['REDIS_PORT_6379_TCP_PORT']
CELERY_REDIS_DB = os.environ['CELERY_REDIS_DB']
CELERY_TRACK_STARTED = True
BROKER_URL = 'redis://{}'.format(CELERY_REDIS_HOST)
