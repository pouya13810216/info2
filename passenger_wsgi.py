import os
import sys

# مسیر تا جایی که info هست
sys.path.insert(0, os.path.expanduser('~/public_html/django/info2'))

# نام ماژول تنظیمات باید info.settings باشه نه info2.settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'info.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
