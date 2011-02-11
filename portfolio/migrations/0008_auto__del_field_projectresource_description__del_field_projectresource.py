# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'ProjectResource.description'
        db.delete_column('portfolio_projectresource', 'description')

        # Deleting field 'ProjectResource.type'
        db.delete_column('portfolio_projectresource', 'type')

        # Adding field 'ProjectResource.name'
        db.add_column('portfolio_projectresource', 'name', self.gf('django.db.models.fields.CharField')(default=1, max_length=255), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'ProjectResource.description'
        db.add_column('portfolio_projectresource', 'description', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'ProjectResource.type'
        db.add_column('portfolio_projectresource', 'type', self.gf('django.db.models.fields.CharField')(default='img', max_length=200), keep_default=False)

        # Deleting field 'ProjectResource.name'
        db.delete_column('portfolio_projectresource', 'name')


    models = {
        'portfolio.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'})
        },
        'portfolio.client': {
            'Meta': {'ordering': "['name']", 'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'})
        },
        'portfolio.project': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'Project'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Category']"}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Client']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['portfolio.Skill']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'portfolio.projectresource': {
            'Meta': {'object_name': 'ProjectResource'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'resources'", 'to': "orm['portfolio.Project']"}),
            'resource': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'portfolio.skill': {
            'Meta': {'object_name': 'Skill'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['portfolio']
