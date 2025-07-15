"""
Django command to wait for the database to be available
"""
import time 
from psycopg2 import OperationalError as Psycopg2Error
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

class Command(BaseCommand):
    """Django command to wait for database"""
    
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        
        while not db_conn:
            try:
                db_conn = connections["default"]
                c = db_conn.cursor()
            except:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database is available!'))
        