import environ

root = environ.Path(__file__) - 3

env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
)

environ.Env.read_env(root('.env'))

DEBUG = env('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'graphene_django',

    'users',
    'challenges',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pycon_ml.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            root('frontend'),
        ],
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

WSGI_APPLICATION = 'pycon_ml.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': env.db(default='sqlite:///{}'.format(root('db.sqlite3'))),
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [{
    'NAME':
    'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
}, {
    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
}, {
    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
}, {
    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
}]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

LOCALE_PATHS = [
    root('locale'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATICFILES_DIRS = [
    root('assets'),
]

STATIC_URL = '/static/'
STATIC_ROOT = root('static')

MEDIA_URL = '/media/'
MEDIA_ROOT = root('media')

AUTH_USER_MODEL = 'users.User'

GRAPHENE = {
    'SCHEMA': 'api.schema.schema'
}
