class Source:
    '''
    Source class to define Source Objects
    '''
    def __init__(self,id,name,description,url):
        self.id=id
        self.name=name
        self.description=description
        self.url=url

class Articles:

    '''
    Articles class that defines articles Objects
    '''

    def __init__(self,title,description,url,urlToImage):
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
