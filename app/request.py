from app import app
import urllib.request,json
from .models import source
from .models import articles

Source=source.Source
Articles=articles.Articles
#Getting api key
api_key= app.config['NEWS_API_KEY']


sources_url=app.config['SOURCES_BASE_URL']
everything_url=app.config['EVERYTHING_BASE_URL']


def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)


    return source_results
