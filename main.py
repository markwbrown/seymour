import os
from dotenv import load_dotenv
import yaml
import psycopg2

# Get the path to the directory this file is in
BASEDIR = os.path.abspath(os.path.dirname(__file__))

with open("docker-compose.yml") as dockerConfig:
    dockerConfigKeys = yaml.safe_load(dockerConfig)
    POSTGRES_PORT = dockerConfigKeys['services']['postgres']['ports'][0].split(':')[0]
    # get env from project root
    load_dotenv(os.path.join(BASEDIR, '.env'))
    PHONE_NUMBER = os.getenv('PHONE_NUMBER')
    PHONE_TYPE = os.getenv('PHONE_TYPE')
    EMAIL = os.getenv('EMAIL')
    POSTGRES_DATABASE = os.getenv('DATABASE')
    # get postgres env from project config
    load_dotenv(os.path.join(BASEDIR, 'docker/local/postgres/.env'))
    POSTGRES_HOST = 'localhost'
    POSTGRES_PORT = os.getenv('POSTGRES_PORT')
    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')


    conn = psycopg2.connect(
        database=POSTGRES_DATABASE, user=POSTGRES_USER, password=POSTGRES_PASSWORD, host=POSTGRES_HOST, port=POSTGRES_PORT
    )
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    cursor.execute("UPDATE public.users_user SET email=%s, twofa_phone=%s, twofa_phone_carrier=%s",
                   (EMAIL, PHONE_NUMBER, PHONE_TYPE));
    conn.commit()
    cursor.close()