from pathlib import Path
from decouple import Csv, config
from dj_database_url import parse as db_url

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], cast=Csv())

INSTALLED_APPS = [
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #GeoDjango and PostGIS
    'django.contrib.gis',
    'leaflet',

    # Other apps
    'django_userforeignkey',

    # Mis apps
    'core',
    'dashboard',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Middleware para insertar userkey atomaticamente a los modelos
    'django_userforeignkey.middleware.UserForeignKeyMiddleware',
]

ROOT_URLCONF = 'obscovid.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'static')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'obscovid.wsgi.application'

DATABASES = {
   'default': config('DATABASE_URL', cast=db_url),
}
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

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

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/La_Paz'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_REDIRECT_URL = '/admin/'
LOGOUT_REDIRECT_URL = '/login/'

LEAFLET_CONFIG = {
    'TILES': 'https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
    'DEFAULT_CENTER': [-21.53335, -64.735522],
    'DEFAULT_ZOOM': 15,
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 18,
    'ATTRIBUTION_PREFIX': '&copy; Contribuidor <a href="https://twitter.com/diegocruztorrez" target="_blank">diegoosvaldo85</a>',
    'RESET_VIEW': False,
    # ( max west/y min, max south/x min, max east/y max, max north/x max )
    # 'SPATIAL_EXTENT': (-64.660741, -21.473155, -64.793895, -21.569041),
}

JAZZMIN_SETTINGS = {
    'site_title': 'Obs COVID-19',
    'site_header': 'COVID-19',
    'site_logo': '/core/images/check-1.png',
    'welcome_sign': '',
    'copyright': 'Observatorio COVID-19',
    'search_model': 'dashboard.paciente',
    'user_avatar': None,

    # Top Menu #
    'topmenu_links': [
        {'name': 'Home',  'url': 'admin:index', 'permissions': ['auth.view_user']},
        # external url that opens in a new window (Permissions can be added)
        # {'name': 'Support', 'url': 'https://github.com/farridav/django-jazzmin/issues', 'new_window': True},
        {'model': 'auth.User'},
        {'app': 'dashboard'},
    ],

    # User Menu #
    'usermenu_links': [
        {'name': 'Ayuda', 'url': 'https://twitter.com/diegocruztorrez', 'new_window': True},
        # {'model': 'auth.user'}
    ],

    # Side Menu #
    'show_sidebar': True,
    'navigation_expanded': True,
    'hide_apps': [],
    'hide_models': ['dashboard.departamento', 'dashboard.municipio',],
    'order_with_respect_to': ['dashboard', 'accounts'],
    'custom_links': {
        'dashboard': [{
            'name': 'Cerrar Sesion', 
            'url': 'core:logout', 
            'icon': 'fa-sign-out-alt',
        }]
    },

    # Iconos personalizados para el menu de apps/models - https://www.fontawesomecheatsheet.com/font-awesome-cheatsheet-5x/
    'icons': {
        'auth': 'fa-users-cog',
        'auth.user': 'fa-user',
        'auth.Group': 'fa-users',

        'dashboard.contacto': 'fa-people-carry',
        'dashboard.departamento': 'fa-map-marker',
        'dashboard.enfermedadbase': 'fa-biohazard',
        'dashboard.entidad': 'fa-clinic-medical',
        'dashboard.especialidad': 'fa-laptop-medical',
        'dashboard.medicamento': 'fa-capsules',
        'dashboard.municipio': 'fa-map-marker-alt',
        'dashboard.paciente': 'fa-bed',
        'dashboard.persona': 'fa-walking',
        'dashboard.historiaclinica': 'fa-edit',
        'dashboard.sintomatologia': 'fa-tired',
        'dashboard.usuario': 'fa-tired',
        'dashboard.tratamiento': 'fa-notes-medical',
        'dashboard.medico': 'fa-user-md',
    },

    # Iconos que se usan cuando no se especifica uno manualmente
    'default_icon_parents': 'fa-chevron-circle-right',
    'default_icon_children': 'fa-circle',

    # UI Tweaks #
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    "show_ui_builder": False,

    # Change view #
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs",},
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",
    "accent": "accent-lightblue",
    "navbar": "navbar-lightblue navbar-dark",
    "no_navbar_border": False,
    "sidebar": "sidebar-dark-lightblue",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False
}