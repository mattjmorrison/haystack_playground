from django.db import models
from django.contrib.admin.models import User

class Blog(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    content = models.TextField()
    pub_date = models.DateField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/admin/blog/blog/%d/" % self.pk

class Tweet(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    tweet = models.CharField(max_length=140)

    def __unicode__(self):
        return self.tweet

    def get_absolute_url(self):
        return "/admin/blog/tweet/%d/" % self.pk