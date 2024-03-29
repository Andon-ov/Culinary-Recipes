import os
from pathlib import Path

from dotenv import load_dotenv
import cloudinary as cloudinary
from django.urls import reverse_lazy

# I'm using this part because I'm using the folder, not just the .env file
dotenv_path = os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))), 'envs', '.env')

load_dotenv(dotenv_path)
# load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = bool(os.environ.get('DEBUG'))
DEBUG = True


ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(' ')

CSRF_TRUSTED_ORIGINS = [f'https://{x}' for x in ALLOWED_HOSTS]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'culinary_recipes.recipes_app',
    'culinary_recipes.auth_app',
    'culinary_recipes.common',

    'cloudinary',
    'embed_video',
    'anymail',

]

MIDDLEWARE = [
    'culinary_recipes.middlewares.handle_exception',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'culinary_recipes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'culinary_recipes.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379',
    }
}

if DEBUG:
    AUTH_PASSWORD_VALIDATORS = []
else:

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EET'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR / 'staticfiles',
)

STATIC_ROOT = '/tmp/culinary_recipes/staticfiles'

cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME', None),
    api_key=os.getenv('CLOUDINARY_API_KEY', None),
    api_secret=os.getenv('CLOUDINARY_API_SECRET', None),
    secure=True,
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = reverse_lazy('sign in')
LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGOUT_REDIRECT_URL = reverse_lazy('index')

AUTH_USER_MODEL = 'auth_app.AppUser'

EMAIL_BACKEND = "anymail.backends.sendinblue.EmailBackend"

ANYMAIL = {
    "SENDINBLUE_API_KEY": os.getenv('API_KEY'),
}

DEFAULT_FROM_EMAIL = "<your email address>"

LOGS_DIR = BASE_DIR / 'Logs'

try:
    os.mkdir(LOGS_DIR)
except:
    pass

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {'()': 'django.utils.log.RequireDebugTrue', },
        'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse', }
    },
    'formatters': {
        'verbose': {
            'format': '{asctime} [{levelname}] {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'formatter': 'verbose',
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'WARNING',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': LOGS_DIR / 'Log.txt',
            'formatter': 'verbose',
            # clear log file after restart - remove for prod
            'mode': 'w',
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': True,
        },
        # 'root': {
        #     'handlers': ['console', 'file'],
        #     'level': 'INFO',
        # },
    },
}
# Local -> DEBUG
# Dev/test server -> Info
# Prod -> Warning/Error
