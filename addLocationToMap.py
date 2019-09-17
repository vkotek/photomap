import boto3
import logging
import exif_reader

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):

    s3 = boto3.client("s3")
    if event:
        
        logger.info(event)
        
        bucket = event['Records'][0]['s3']['bucket']['name']
        logger.info(bucket)
        
        file_object = event['Records'][0]
        key = str( file_object['s3']['object']['key'] )
        s3.download_file('vkotek-geocam', key, '/tmp/{}'.format(key))
        
        result = exif_reader.get_gps_from_file('/tmp/{}'.format(key))
        
        logger.info(result)

    return "Success!?"
