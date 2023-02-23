import requests
from bs4 import BeautifulSoup
import json

def lambda_handler(event, context):
    # Parse JSON input
    input_json = json.loads(event['body'])
    url = input_json['url']
    direct_page_url = input_json['direct_page_url']
    class_id = input_json['class_id']
    div_tag_id = input_json['div_tag_id']
    
    # Crawl webpage
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    # Find elements on page
    elements = soup.find_all(class_=class_id)
    results = []
    for element in elements:
        if element.has_attr('id') and element['id'] == div_tag_id:
            results.append(element.text.strip())
    
    # Prepare output JSON object
    output_json = {
        'name': input_json['name'],
        'url': url,
        'direct_page_url': direct_page_url,
        'class_id': class_id,
        'div_tag_id': div_tag_id,
        'results': results
    }
    
    # Call external API with output JSON object
    api_url = 'https://example.com/api'
    response = requests.put(api_url, json=output_json)
    
    return {
        'statusCode': 200,
        'body': json.dumps(output_json)
    }
