from flask import render_template
from app import app
from .request import get_source

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #Getting news sources
    general_source=get_source('general')
    business_source=get_source('business')
    entertainment_source=get_source('entertainment')
    technology_source=get_source('technology')
    sports_source=get_source('sports')
    title= 'Get the latest news'
    return render_template('index.html', title=title,general=general_source,business=business_source,entertainment=entertainment_source,technology=technology_source,sports=sports_source)


@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)
