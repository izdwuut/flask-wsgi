import sys

sys.path.insert(0, '/var/www/flask-wsgi/')

from app import create_app
application = create_app()
