from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Imports an SQL file to the database'

    def add_arguments(self, parser):
        parser.add_argument('sql_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for sql_file in options['sql_file']:
            with open(sql_file, 'r') as f:
                sql = f.read()
                with connection.cursor() as cursor:
                    cursor.execute(sql)
