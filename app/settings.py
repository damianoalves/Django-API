# -*- coding: utf-8 -*-
import os
from os import environ as env

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '%h@e@itau5+7ml6kuuupgg^j%h+&8*04vu-r90ey17foxn-icd'
SITE_ID = 1
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'oauth2_provider',
    'django_filters',
    'corsheaders',
    'guardian',

    'rest_auth',
    'rest_auth.registration',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.google',

    'access'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

# POSTGRES
DB_ENGINE = 'django.db.backends.postgresql'
DB_NAME = env.get('DJANGO_DB_NAME', 'postgres')
DB_USER = env.get('DJANGO_DB_USER', 'postgres')
DB_PASSWORD = env.get('DJANGO_DB_PASSWORD', 'postgres')
DB_HOST = env.get('DJANGO_DB_HOST', 'localhost')
DB_PORT = env.get('DJANGO_DB_PORT', '5432')

DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}

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
DATE_FORMAT = 'd/m/Y'
DATETIME_FORMAT = 'd/m/Y - H:i:s'
LANGUAGE_CODE = 'en-us'
LANGUAGES = (('en-us', u'English'),)
TIME_ZONE = 'America/Araguaina'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Email
SERVER_EMAIL = 'Damiano Alves <damiano.alves@gmail.com>'
DEFAULT_FROM_EMAIL = env.get('DEFAULT_FROM_EMAIL', SERVER_EMAIL)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST = env.get('EMAIL_HOST', 'smtp.sendgrid.net')
EMAIL_PORT = env.get('EMAIL_PORT', '587')
EMAIL_HOST_USER = env.get('EMAIL_HOST_USER', 'apikey')
EMAIL_HOST_PASSWORD = env.get('EMAIL_HOST_PASSWORD', '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')

# REST FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,
    'EXCEPTION_HANDLER': 'core.errors.custom_exception_handler',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FileUploadParser'
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

# ALLAUTH
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_CONFIRMATION_HMAC = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN = 60
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'confirm/'
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'confirm/'
ACCOUNT_EMAIL_SUBJECT_PREFIX = ''
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 3
LOGIN_REDIRECT_URL = '/home'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v7.0',
    }

}

# REST AUTH
OLD_PASSWORD_FIELD_ENABLED = True
LOGOUT_ON_PASSWORD_CHANGE = False


AUTHENTICATION_BACKENDS = (
    'oauth2_provider.backends.OAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend'
)

OAUTH2_PROVIDER = {
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
}

# GUARDIAN
GUARDIAN_RAISE_403 = True
ANONYMOUS_USER_NAME = None

# CORS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'x-api-key',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)
