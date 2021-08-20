import json
import urllib.parse
import boto3

s3 = boto3.client('s3')

transcoder = boto3.client('elastictranscoder')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    response = transcoder.create_job(
    PipelineId='1628779394709-mkrsir',
    
    Input={
        'Key': key,
        'FrameRate': 'auto',
        'Resolution': 'auto',
        'AspectRatio': 'auto',
        'Interlaced': 'auto',
        'Container': 'auto',
    },

    Outputs=[
        {
            'Key': key + '.mp4',
            'Rotate': 'auto',
            'PresetId': '1351620000001-000010',
        },
    ],

)