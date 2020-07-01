from logging import LogRecord

logging = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s | %(levelname)s | %(module)s | %(name)s: %(message)s'
        },
    },

    "filters": {
        "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"},
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },

        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'info.log',
            'formatter': 'verbose',
        },

        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "filters": ["require_debug_false"],
        },
    },
    'loggers': {
        'django': {
            'level': 'INFO',
            'handlers': ['console', 'file'],
            'propagate': True,
        },
        'django.request': {
            'level': 'INFO',
            'handlers': ['console', 'file'],
            'propagate': True,
        },

        'django.security.*': {
            'level': 'INFO',
            'handlers': ['console', 'file'],
            'propagate': True,
        },
    },
}


def filter_400(record: LogRecord) -> bool:
    return record.status_code != 400