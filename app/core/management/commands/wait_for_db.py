"""
Django command to wait for the database to be available
"""
import time

from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for the db"""

    def handle(self, *args, **options):
        """Entry point for call"""
        self.stdout.write('Waiting for the database....')
        db_up=False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout("Database unavailable, waiting 1 sec...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database is UP and OK'))


