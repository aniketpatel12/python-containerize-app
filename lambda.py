import json
import boto3

def handler(event, context):
    s3_client = boto3.client('s3')
    s3_clientObj = s3_client.get_object(Bucket='demo-temp-bucket', Key = 'datafile.txt')

    for line in s3_clientObj['Body'].iter_lines():
        obj = json.loads(line)
        print(f"Name: {obj['Name']['Fnm']} ID: {obj['id']['n']}")
    print("Execution of your lambda function is Completed !")
