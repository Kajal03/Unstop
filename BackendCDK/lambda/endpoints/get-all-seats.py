import json
import boto3
from constants.database_constants import DB_CREDENTIALS_SECRET_STORE_ARN, DATABASE_NAME, DB_CLUSTER_ARN
from constants.status_code_constants import OK
from helperUtils.httpUtils import http_response

rds_client = boto3.client('rds-data')

def lambda_handler(event, context):
    response = execute_statement('SELECT * FROM unstop_db.SEATS')
    return http_response(OK, json.dumps(response))


def execute_statement(sql):
    response = rds_client.execute_statement(
        secretArn=DB_CREDENTIALS_SECRET_STORE_ARN,
        database=DATABASE_NAME,
        resourceArn=DB_CLUSTER_ARN,
        sql=sql
    )
    records = response['records']

    table_columns = ['isBooked', 'seatNum', 'user_email']
    all_seats = []
    for record in records:
        item = {}
        for i, value in enumerate(record):
            column_name = table_columns[i]
            item[column_name] = value.get('stringValue') or value.get('longValue') or value.get('booleanValue')
        all_seats.append(item)
    
    return all_seats