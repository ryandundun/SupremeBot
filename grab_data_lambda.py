import json
import requests
from bs4 import BeautifulSoup

import boto3

def lambda_handler(event, context):
    #Grab Supreme web contents
    page = 'https://www.supremenewyork.com/shop'
    page_json = 'https://www.supremenewyork.com/shop.json'
    r = requests.get(page, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'})
    soup = BeautifulSoup(r.content, "html.parser")

    #get the correct spot from the configuration file
    bucket = s3_resource.Bucket('hype-data')
    bucket.put_object(Body=page, ContentType='image/png', Key='' + str(theIndex))
    bucket.put_object(Body=page, ContentType='image/png', Key='wordcloud' + str(theIndex))

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
        # 'supremehtml': r.content
        # 'supremejson': page_json
    }
