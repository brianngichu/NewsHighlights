import unittest
from models import articles
Articles=articles.Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_article = Articles("Title of the article",'description of the article','https://abcnews.go.com/theview/video/andrea-kelly-details-allegations-abuse-husband-kelly-58286731','https://s.abcnews.com/images/theview/181004_view_andrea_1134_hpMain_16x9_992.jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

if __name__ == '__main__':
    unittest.main()
