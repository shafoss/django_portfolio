"""
Script to create the database specified in settings.
"""
import psycopg2
from django.conf import settings
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import OperationalError

dbname = settings.DATABASES['default']['NAME']
user = settings.DATABASES['default']['USER']
password = settings.DATABASES['default']['PASSWORD']


def setup_database():
    global conn
    try:
        conn = psycopg2.connect(
            "dbname='postgres' user='" + user + "' password='" + password + "' host='localhost' port='5432'")
        # set the proper isolation level so CREATE DATABASE works
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        with conn.cursor() as cur:
            # execute SQL in here
            cur.execute("CREATE DATABASE " + dbname)
            cur.execute("GRANT ALL PRIVILEGES ON DATABASE " + dbname + " TO " + user)
    except OperationalError:
        # if the user defined in settings hasn't been created yet, log in with a valid user instead.
        other_user = input("Enter username: ")
        other_password = input("Enter password: ")
        conn = psycopg2.connect(
            "dbname='postgres' user='" + other_user + "' password='" + other_password + "' host='localhost' port='5432'")
        # set the proper isolation level so CREATE DATABASE works
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        with conn.cursor() as cur:
            # execute SQL in here
            cur.execute("CREATE ROLE " + user + " WITH LOGIN PASSWORD '" + password + "'")
            cur.execute("ALTER USER " + user + " CREATEDB")
            cur.execute("CREATE DATABASE " + dbname)
            cur.execute("GRANT ALL PRIVILEGES ON DATABASE " + dbname + " TO " + user)
    finally:
        conn.close()


if __name__ == '__main__':
    setup_database()
