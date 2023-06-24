import json
import boto3
from constants.database_constants import DB_CREDENTIALS_SECRET_STORE_ARN, DATABASE_NAME, DB_CLUSTER_ARN
from constants.status_code_constants import OK
from helperUtils.httpUtils import http_response

rds_client = boto3.client('rds-data')

def lambda_handler(event, context):
    response = execute_statement('SELECT seatNum FROM unstop_db.SEATS where isBooked=0')
    return http_response(OK, json.dumps(response))


def execute_statement(sql):
    response = rds_client.execute_statement(
        secretArn=DB_CREDENTIALS_SECRET_STORE_ARN,
        database=DATABASE_NAME,
        resourceArn=DB_CLUSTER_ARN,
        sql=sql
    )
    records = response['records']

    all_available_seats = []
    for record in records:
        for value in record:
            all_available_seats.append(value.get('stringValue') or value.get('longValue') or value.get('booleanValue'))

    return all_available_seats