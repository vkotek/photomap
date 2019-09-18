import boto3
import logging, datetime
import exif_reader, save_to_file

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

        # Get only filename for tmp location
        key_tmp = key.split("/")[-1]
        
        s3.download_file('vkotek-geocam', key, '/tmp/{}'.format(key_tmp))
        logger.info("File downloaded to /tmp/{}".format(key_tmp))
        
        gps = exif_reader.get_gps_from_file('/tmp/{}'.format(key_tmp))
        
        data = [key_tmp, datetime.datetime.utcnow().isoformat(), gps[0], gps[1]]
        
        save_to_file.save(data, s3)
        logger.info("Updated CSV file in s3.")

    return "Success!?"
