from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'Generate random users'

    def add_arguments(self, parser):

        #positional argument
        parser.add_argument('count', type=int, help='Indicate the number of users to be created')


        #named/optional argument
        parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix')

        #boolean argument
        parser.add_argument('-s','--superuser', action='store_true', help='Create a superuser account')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        prefix = kwargs['prefix']
        superuser = kwargs['superuser']
        for i in range(count):
            if prefix:
                username = f'{prefix}_{get_random_string()}'
            else:
                username = get_random_string()

            if superuser:
                User.objects.create_superuser(username=username, email='superuser@gmail.com', password='hello@123')
            else:
                User.objects.create_user(username=username, email='hello@gmail.com', password='hello@123')
