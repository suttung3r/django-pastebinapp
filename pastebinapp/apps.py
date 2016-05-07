from django.apps import AppConfig
from .tasks import start


class PastebinappConfig(AppConfig):
    name = 'pastebinapp'

    def ready(self):
        print('calling ready')
        start()
