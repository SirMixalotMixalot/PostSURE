import os
import psycopg2
import json
import numpy
from json import JSONEncoder
from datetime import datetime 
import os
pg_conn_string = os.environ["DATABASE_URL"]
print(pg_conn_string)
class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

def create_table():
    with psycopg2.connect(pg_conn_string) as conn:

        with conn.cursor() as cur:

            cur.execute("CREATE TABLE masks (mask json, time timestamp, score integer );")
            
            conn.commit()




def pushes_mask_to_database(mask, score):
    dt = datetime.now()
    timestamp = datetime.timestamp(dt)
    mask_data = {"array" : mask}
    encoded_mask = json.dumps(mask_data, cls=NumpyArrayEncoder)
    with psycopg2.connect(pg_conn_string) as conn:

        with conn.cursor() as cur:

            cur.execute("INSERT INTO masks (mask, time, score) VALUES (%s, %s, %s)",
           (encoded_mask, timestamp, score))
            
            conn.commit()

def database_mask_to_normal_mask(database_values):
    db_mask = database_values[0]
    normal_mask = json.loads(db_mask)
    return (normal_mask, database_values[1], database_values[2])


def get_mask_and_timestamp_from_database():
    with psycopg2.connect(pg_conn_string) as conn:
        with conn.cursor() as cur:
            results = cur.execute("SELECT (mask,time,score) from masks").fetchall()

            conn.commit()
            return map(database_mask_to_normal_mask, results)
        





