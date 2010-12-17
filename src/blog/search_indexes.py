from haystack import indexes
from haystack import site
from blog.models import Blog, Tweet

class BlogIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    pub_date = indexes.DateField(model_attr='pub_date')
    user = indexes.CharField(model_attr='user')

site.register(Blog, BlogIndex)

class TweetIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    tweet = indexes.CharField(model_attr='tweet')
    user = indexes.CharField(model_attr='user')

site.register(Tweet, TweetIndex)