# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Client'
        db.create_table('portfolio_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=250)),
        ))
        db.send_create_signal('portfolio', ['Client'])

        # Adding model 'ProjectResource'
        db.create_table('portfolio_projectresource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('resource', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.Project'])),
        ))
        db.send_create_signal('portfolio', ['ProjectResource'])

        # Adding model 'Skill'
        db.create_table('portfolio_skill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('portfolio', ['Skill'])

        # Adding field 'Project.created'
        db.add_column('portfolio_project', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2011, 2, 8, 12, 58, 39, 198932), blank=True), keep_default=False)

        # Adding field 'Project.client'
        db.add_column('portfolio_project', 'client', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['portfolio.Client']), keep_default=False)

        # Adding M2M table for field skills on 'Project'
        db.create_table('portfolio_project_skills', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['portfolio.project'], null=False)),
            ('skill', models.ForeignKey(orm['portfolio.skill'], null=False))
        ))
        db.create_unique('portfolio_project_skills', ['project_id', 'skill_id'])


    def backwards(self, orm):
        
        # Deleting model 'Client'
        db.delete_table('portfolio_client')

        # Deleting model 'ProjectResource'
        db.delete_table('portfolio_projectresource')

        # Deleting model 'Skill'
        db.delete_table('portfolio_skill')

        # Deleting field 'Project.created'
        db.delete_column('portfolio_project', 'created')

        # Deleting field 'Project.client'
        db.delete_column('portfolio_project', 'client_id')

        # Removing M2M table for field skills on 'Project'
        db.delete_table('portfolio_project_skills')


    models = {
        'portfolio.client': {
            'Meta': {'ordering': "['name']", 'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'})
        },
        'portfolio.project': {
            'Meta': {'object_name': 'Project'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Client']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['portfolio.Skill']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'})
        },
        'portfolio.projectresource': {
            'Meta': {'object_name': 'ProjectResource'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Project']"}),
            'resource': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'portfolio.skill': {
            'Meta': {'object_name': 'Skill'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['portfolio']
