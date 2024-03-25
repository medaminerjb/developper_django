import static files 
```
python manage.py collectstatic
```
In your Django project's settings file (`settings.py`), make sure the following settings are correctly configured:
```python
# settings.py 
# Define the path where static files will be collected
STATIC_ROOT = '/path/to/your/static/folder/'
# Define the URL prefix for static files 
STATIC_URL = '/static/'
```
in your django project urls file (urls.py),make changes 
```python
# urls.py 
from django.conf import settings
from django.conf.urls.static import 
static urlpatterns = [ 
# Your URL patterns here
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```