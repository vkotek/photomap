import boto3, csv

key = 'geopoints.csv'
key_path = '/tmp/{}'.format(key)
bucket = 'vkotek-geocam'

def save(data, client):
    
    # Download remote CSV from s3
    try:
        client.download_file(bucket, key, key_path)
    except:
        print("File not found on s3, creating new file.")
    
    # Append new line to local temp file
    with open(key_path, 'a') as f:
        writer = csv.writer(f, delimiter="|")
        writer.writerow(data)
        
    file_object = open(key_path, 'rb')

    # Load the updated CSV to s3
    result = client.put_object(
        Body=file_object,
        Bucket='vkotek-geocam',
        Key='geopoints.csv')
        
    file_object.close()
    
    return result