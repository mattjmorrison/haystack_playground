import datetime
from haystack.indexes import *
from haystack import site
from blog.models import Blog

class BlogIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    pub_date = DateTimeField(model_attr='pub_date')

    def get_queryset(self):
        """Used when the entire index for model is updated."""
        return Blog.objects.filter(pub_date__lte=datetime.datetime.now())

site.register(Blog, BlogIndex)