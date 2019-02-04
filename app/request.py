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
