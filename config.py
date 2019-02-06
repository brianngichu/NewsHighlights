import os

class Config:
    SOURCES_BASE_URL='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    EVERYTHING_BASE_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_API_KEY= os.environ.get('NEWS_API_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options= {
    'development':DevConfig,
    'production':ProdConfig
}
