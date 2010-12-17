# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Tweet'
        db.create_table('blog_tweet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tweet', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal('blog', ['Tweet'])


    def backwards(self, orm):
        
        # Deleting model 'Tweet'
        db.delete_table('blog_tweet')


    models = {
        'blog.blog': {
            'Meta': {'object_name': 'Blog'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'blog.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tweet': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['blog']
