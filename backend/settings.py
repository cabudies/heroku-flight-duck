"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
from decouple import config
import os
import dj_database_url
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "#0n&@9r(69=*_p)0%j3-bc_8dtb*y6(krj(^!rvgdmoz*h$nd$"
# SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'flight-duck-backend-env.eba-chkzqkeu.us-west-2.elasticbeanstalk.com',
    '.herokuapp.com'
]


# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    # 'backend.apps.CustomAdminConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.sites',
    # 'api',
    'users',
    'flights',
    'hotels',
    # rest framework and cors
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    # social accounts
    'oauth2_provider',
    'social_django',
    'drf_social_oauth2',
    # import export user data
    'import_export'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Oauth
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # drf_social_oauth2
    'drf_social_oauth2.backends.DjangoOAuth2',

    # 'django.contrib.auth.backends.ModelBackend',
    # 'allauth.account.auth_backends.AuthenticationBackend',

    # Facebook OAuth2
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',

    'django.contrib.auth.backends.ModelBackend',
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'flight_duck',
#         'USER': 'postgres',
#         'PASSWORD': 'gurjas',
#         'HOST': 'localhost',
#         'PORT': '5432'
#     }
# }

# if 'RDS_DB_NAME' in os.environ:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql',
#             'NAME': os.environ['RDS_DB_NAME'],
#             'USER': os.environ['RDS_USERNAME'],
#             'PASSWORD': os.environ['RDS_PASSWORD'],
#             'HOST': os.environ['RDS_HOSTNAME'],
#             'PORT': os.environ['RDS_PORT']
#         }
#     }
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         }
#     }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd9acdmabn2p185',
        'USER': 'gcmxdegrskqmtw',
        'PASSWORD': '8a3831d1cc0bc4fb670fa88b79bf663573c6dd52e2b98513f1fb750be51f8b83',
        'HOST': 'ec2-52-204-72-14.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

WHITENOISE_USE_FINDERS = True

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'backend/static')
# ]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTH_USER_MODEL = "users.NewUser"
# LOGIN_REDIRECT_URL = 'home'
# LOGOUT_REDIRECT_URL = 'home'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = ('content-disposition', 'accept-encoding', 'content-type', 
'accept', 'origin', 'authorization', 'user-id')

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # oauth
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'drf_social_oauth2.authentication.SocialAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.AllowAny',
    ]
}

SITE_ID = 2

# Facebook configuration
# SOCIAL_AUTH_FACEBOOK_KEY = config('SOCIAL_AUTH_FACEBOOK_KEY')
# SOCIAL_AUTH_FACEBOOK_SECRET = config('SOCIAL_AUTH_FACEBOOK_SECRET')
# SOCIAL_AUTH_GOOGLE_PLUS_KEY = config('SOCIAL_AUTH_GOOGLE_PLUS_KEY')
# SOCIAL_AUTH_GOOGLE_PLUS_SECRET = config('SOCIAL_AUTH_GOOGLE_PLUS_SECRET')
SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('SOCIAL_AUTH_FACEBOOK_SECRET')
SOCIAL_AUTH_GOOGLE_PLUS_KEY = os.environ.get('SOCIAL_AUTH_GOOGLE_PLUS_KEY')
SOCIAL_AUTH_GOOGLE_PLUS_SECRET = os.environ.get('SOCIAL_AUTH_GOOGLE_PLUS_SECRET')

SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'http://localhost:3000/'

# Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from Facebook.
# Email is not sent by default, to get it, you must request the email permission.
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, first_name, last_name, email'
}
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile', 'openid']
SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ['email', 'first_name', 'last_name']
SOCIAL_AUTH_USER_FIELDS = ['email', 'first_name', 'last_name']

IMPORT_EXPORT_IMPORT_PERMISSION_CODE = 'delete'
IMPORT_EXPORT_EXPORT_PERMISSION_CODE = 'delete'
DEFAULT_AUTO_FIELD='django.db.models.AutoField'

django_heroku.settings(locals())