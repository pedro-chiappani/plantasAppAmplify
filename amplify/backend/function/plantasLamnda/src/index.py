import json
import datetime

def handler(event, context):

    cuerrent_time = datetime.datetime.now().time()
    body = {
        'message' : 'Hola, la hora es: ' + str(cuerrent_time)
    }
    
    print('received event:')
    print(event)

    response = {
        'statusCode': 200,
        'body': json.dumps(body),
        'headers': {
            'Content-Type': 'application/json',
            'Acces-Control-Allow-Origin': '*'
        },
    }

    return response
