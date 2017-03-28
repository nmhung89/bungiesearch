from django.core.management import call_command
from django.core.management.base import BaseCommand

from ._utils import option_list


class Command(BaseCommand):
    help = "Rebuilds the search index by clearing the search index and then performing an update."
    option_list = option_list

    def handle(self, *args, **options):
        call_command('clear_index', **options)
        call_command('search_index', action='update', **options)
