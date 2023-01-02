from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Remove Users'

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int, help='User Id')

    def handle(self, *args, **kwargs):
        user_ids = kwargs['user_id']
        for user_id in user_ids:
            try:
                user = User.objects.get(pk=user_id)
                user.delete()
                #self.stdout.write(f'{user.username} with id {user_id} removed successfully!')
                self.stdout.write(self.style.SUCCESS(f'{user.username} with id {user_id} removed successfully!'))
            except User.DoesNotExist:
                #self.stdout.write(f'User with id {user_id} does not exist')
                self.stdout.write(self.style.WARNING(f'User with id {user_id} does not exist'))
