from django.core.management.base import BaseCommand
from optparse import make_option


option_list = BaseCommand.option_list + (
    make_option(
        '--noinput',
        action='store_false',
        dest='interactive',
        default=True,
        help='If provided, no prompts will be issued to the user and the data will be wiped out'
    ),
    make_option(
        '--guilty-as-charged',
        action='store_true',
        dest='confirmed',
        default=False,
        help='Flag needed to confirm the clear index.'
    ),
    make_option(
        '--timeout',
        action='store',
        dest='timeout',
        default=None,
        type=int,
        help='Specify the timeout in seconds for each operation.'
    )
)
