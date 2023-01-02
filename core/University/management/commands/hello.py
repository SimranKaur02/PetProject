from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Display Hello.'


    def handle(self, *args, **kwargs):
        print('Hello World!!')
        # self.stdout.write('Hello')