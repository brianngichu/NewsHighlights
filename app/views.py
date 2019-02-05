from flask import render_template
from app import app
from .request import get_sources

# Views
@app.route('/')
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


@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)
