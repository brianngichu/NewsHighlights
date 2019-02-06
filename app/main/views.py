from flask import render_template,request,redirect,url_for
# from app import app
from . import main
from ..request import get_sources,get_articles
from ..models import Source,Articles

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #Getting news sources
    general_sources=get_sources('general')
    business_sources=get_sources('business')
    entertainment_sources=get_sources('entertainment')
    technology_sources=get_sources('technology')
    sports_sources=get_sources('sports')
    print(general_sources)
    title= 'Get the latest news'
    return render_template('index.html',title=title,general=general_sources,business=business_sources,entertainment=entertainment_sources,technology=technology_sources,sports=sports_sources)


@main.route('/articles/<source_id>')
def articles(source_id):

    '''
    View news page function that returns the news details page and its data
    '''
    # Fetching articles
    articles= get_articles(source_id)
    #title=f'{articles.title}'

    title=f'{source_id}'

    return render_template('articles.html',id = source_id,articles=articles,title=title)
