"""
Django settings for nimushop project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku
import dj_database_url
import cloudinary
from decouple import config


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's%o-cymq=tk9%-(t7nwqjivqz!pc3e-4ksw1!hkaa%!bz%p4a5'

# SECURITY WARNING: don't run with debug turned on in production!



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    
    'crispy_forms',
    'django_countries',
    'cloudinary_storage',
    'cloudinary',
     
    'taggit',
    'core'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


]

ROOT_URLCONF = 'nimushop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'nimushop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
    
#     'default': {
        
#         'ENGINE': 'django.db.backends.sqlite3',
        
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   
#    }

# }
# DATABASES = {
#     'default': dj_database_url.config()
        
#     }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'static_in_env/img')

# Auth

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'

# CRISPY FORMS

CRISPY_TEMPLATE_PACK = 'bootstrap4'


SOCIALACCOUNT_PROVIDERS = {
    'facebook':
     
        {
         'METHOD': 'oauth2',
         'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
         'SCOPE': ['email', 'public_profile'],
         'AUTH_PARAMS': {'auth_type': 'authenticate'},
         'INIT_PARAMS': {'cookie': True},
         'FIELDS': [
             'id',
             'first_name',
             'last_name',
             'name',
             'name_format',
             'picture',
             'short_name'
         ],
         'EXCHANGE_TOKEN': True,
         'LOCALE_FUNC': lambda request: 'ru_RU',
         'VERIFIED_EMAIL': False,
         'VERSION': 'v7.0',
         # you should fill in 'APP' only if you don't create a Facebook instance at /admin/socialaccount/socialapp/
         'APP': {
             'client_id': '834810577213058',  # !!! THIS App ID
             'secret': '8499919a6c473d1192c50603203af535',  # !!! THIS App Secret
             'key': ''
                }
         }
}
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_USERNAME_REQURIED=True
ACCOUNT_FORMS = {
'signup': 'core.forms.CustomSignupForm',
}

ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False  # a personal preference. True by default. I don't want users to be interrupted by logging in
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'  # a personal preference. I don't want to add 'i don't remember my username' like they did at Nintendo, it is stupid

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True          #* It's not working for some reason but I don't know why, we have Handled from forms.py 

ACCOUNT_USERNAME_REQUIRED = True

#* to solve subdomain users login for now
ACCOUNT_EMAIL_VERIFICATION = 'optional' # to send mail for subscribers not to created users but it doesn't fix the issue

ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = None # To prevent login on verification for created users but the subscribers affected    

# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/auth/email/success/'  

# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/'                 

ACCOUNT_CONFIRM_EMAIL_ON_GET = True  # try to solve the issue

ACCOUNT_SESSION_REMEMBER = True

ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'gen:email_success'  # a page to identify that email is confirmed when not logged in
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'gen:email_success'  # same but logged in

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7  # a personal preference. 3 by default

ACCOUNT_LOGIN_ON_PASSWORD_RESET = True  # False by default
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True  # True by default
# ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login'
ACCOUNT_USERNAME_BLACKLIST = ['yomama',]
ACCOUNT_USERNAME_MIN_LENGTH = 4  # a personal preference
ACCOUNT_SESSION_REMEMBER = True  # None by default (to ask 'Remember me?'). I want the user to be always logged in

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL = 'floydphuti911@gmail.com'
EMAIL_HOST_PASSWORD = 'Floydfuckme-3'

EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR,"sent_emails")
UNIQUE_EMAIL = True  # just to be sure, ok

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


STRIPE_LIVE_PUBLIC_KEY= 'your-live-public-key'
STRIPE_LIVE_SECRET_KEY= 'your-live-secret-key'
STRIPE_TEST_PUBLIC_KEY= 'your-test-public-key'
STRIPE_TEST_SECRET_KEY= 'your-test-secret-key'

STRIPE_PUBLIC_KEY = "pk_live_51Jhe9KI0vyNNQbJ57WEnLY1c81XYIcBD0InuUvdY8JOobsuEUA7P7ZVrE4mmqNXWCmwEwMXaqQlyIttKcOUw024Q008XJKF7Pd"
STRIPE_SECRET_KEY = "sk_test_51Jhe9KI0vyNNQbJ56RMDp4moQoQsEx3KUwaNQ5J3WQOn31rvyBaDvAh2bApMS4EmiLAJhj3lzoxMkQW4HHB9afzN00iA7dw43u"

# Activate Django-Heroku.
django_heroku.settings(locals())
