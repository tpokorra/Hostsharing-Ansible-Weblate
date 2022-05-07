# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{django_secret_key}}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ADMINS = [('{{admin_name}}', '{{admin_email}}')]
SERVER_EMAIL = 'no-reply@{{domain}}'
EMAIL_SUBJECT_PREFIX = '[{{email_prefix}}]'

ALLOWED_HOSTS = [".{{domain}}"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{pac}}_{{user}}',
        'USER': '{{pac}}_{{user}}',
        'PASSWORD': '{{password}}',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

ACCOUNT_ACTIVATION_DAYS = 1
REGISTRATION_OPEN = False
DEFAULT_FROM_EMAIL = 'no-reply@{{domain}}'
EMAIL_HOST = '{{SMTP_HOST}}'
EMAIL_PORT = {{SMTP_PORT}}
EMAIL_HOST_USER = '{{SMTP_USER}}'
EMAIL_HOST_PASSWORD = '{{SMTP_PWD}}'
EMAIL_USE_TLS = True

DEFAULT_FRONTEND_LANGUAGE = 'DE'
AVAILABLE_FRONTEND_LANGUAGES = ['EN', 'DE']
