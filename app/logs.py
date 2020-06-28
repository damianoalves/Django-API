from logging import LogRecord

logging = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s | %(levelname)s | %(module)s | %(message)s'
        },
        'simple': {
            'format': '%(asctime)s | %(levelname)s | %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },

        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'info.log',
            'formatter': 'verbose'
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