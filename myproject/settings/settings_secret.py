import os

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mswatzell',
        'USER': 'mswatzell',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%$*cg^l8)0k!0ul03@d&^_jk7rt_&5gab+&nc6-=p+zl&0$+$e'
