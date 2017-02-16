from .common import *

DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DATABASES = {
    'default' : {
    'ENGINE' : 'django.db.backends.mysql',
    'HOST': 'duojing.mysql.pythonanywhere-services.com',
    'NAME': 'duojing$default',
    'USER': 'duojing',
    'PASSWORD' : '950711ju',
    'OPTIONS': {
    'sql_mode': 'traditional',
    },
},

}