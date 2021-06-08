from django.core.management.base import BaseCommand
from django_q.models import Schedule


class Command(BaseCommand):
    help = 'Schedule actions'

    def handle(self, *args, **options):
        Schedule.objects.update_or_create(
            name='report_last_minute_actions',
            defaults=dict(
                func='mediaserver.mediaserver_api.report_last_minute_actions',
                schedule_type='I',
                minutes=1,
                repeats=-1
            )
        )
