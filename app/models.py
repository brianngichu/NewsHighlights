class Source:
    '''
    Sources class that defines source Objects
    '''

    def __init__(self,id,name,title,description,url):
        self.id =id
        self.name=name
        self.category=category
        self.description = description
        self.url = url




class Article:

    '''
    Aticle class that defines article Objects
    '''

    def __init__(self,title,description,url,urlToImage):
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
