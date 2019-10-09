from django.core.management import BaseCommand


class Command(BaseCommand):
    args = ''
    help = 'Export data to remote server'

    def add_arguments(self, parser):
        pass


