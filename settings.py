#tsoporan.com settings.

import os

HERE = os.path.abspath(os.path.dirname(__file__))
DEBUG = False 
TEMPLATE_DEBUG = DEBUG
ADMINS = (('Your Name', 'your_email@domain.com'),)
MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': os.path.join(HERE, 'tsoporan.db'),                      
        'USER': '',                      
        'PASSWORD': '',                  
        'HOST': '',                      .
        'PORT': '',                      
    }
}
TIME_ZONE = 'America/Toronto'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = True
MEDIA_ROOT = HERE + '/static/'
MEDIA_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
SECRET_KEY = 'AKJSKJKGAKGJAKSGJKAGJAKSGJKAJGKLDJI&@@U#IO@#*'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
ROOT_URLCONF = 'tsoporan.urls'

TEMPLATE_DIRS = (
    HERE + '/templates',
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'south', 
)
#Load sensitive settings.
execfile(os.path.join(HERE), '.private-settings'))
