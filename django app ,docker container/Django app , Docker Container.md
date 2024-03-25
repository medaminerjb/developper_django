
## **--Django app--**
### Setup :
**Install Python:**
If you haven't installed Python yet, download and install it from the official Python website: [python.org](https://www.python.org/downloads/). Make sure to add Python to your system's PATH during installation.
**Install Virtualenv :** . Install `virtualenv` using pip:
```shell
pip install virtualenv
```
**Create a Virtual Environment :** Create a new virtual environment for your project. :
```shell
virtualenv venv
```
**Activate the Virtual Environment:** Activate the virtual environment. 
```shell
source venv/bin/activate
```
**Install Django:** Install Django :
```shell
pip install django
```
**Create a Django Project:** Create a new Django project. Replace example with your choices project name:
```shell
django-admin startproject exemple
```
**Navigate to Project Folder:** enter into the project folder:
```shell
cd exemple
```
**Create a Django App:** replace example within your project name
```shell
python manage.py startapp exemple
```
**Install MySQL Client for Python:** Install the MySQL client for Python using pip:
```shell
pip install mysqlclient
```

**Add the App to Installed Apps:** Open the `settings.py` file in your project directory (example/settings.py`) and add your app to the `INSTALLED_APPS` list:
```python
INSTALLED_APPS = [
    ...
    'exemple',
]```

**Configure Database Settings:** Open the `settings.py` file in your project directory (`project_name/settings.py`). Update the `DATABASES` setting to use MySQL:
```python
DATABASES = { 'default':
			 { 'ENGINE': 'django.db.backends.mysql',
			   'NAME': 'your_database_name',
			   'USER': 'your_mysql_username', 
			   'PASSWORD': 'your_mysql_password',
			    'HOST': 'localhost',# Or the IP address of your MySQL server  
			    'PORT': '3306', # Or the port your MySQL server is running on } }
						  ```
**Configure Settings for Internationalization (i18n):** Open the `settings.py` file in your project directory (`project_name/settings.py`). Add the following settings:
```python
# settings.py
MIDDLEWARE = [
    ...
    'django.middleware.locale.LocaleMiddleware',
    ...
]

# Internationalization
LANGUAGES = [
    ('en', 'English'),
    ('fr', 'French'),
    # Add more languages as needed
]

# Set the default language
LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
```
**Create Translation Files:** Run the following command to create translation files for your app (replace `app_name` with your app's name):
 python manage.py makemessages -l fr  # for French
```shell
  python manage.py makemessages -l xx # tow caractere from language name
```
**Translate Strings:** Open the `.po` file created in the `locale` directory and translate the strings:
```po
msgid "message" 
msgstr "message"
```
**Use Translated Strings in Templates:** In your templates, use the `trans` template tag to mark strings for translation:
```html
{% load i18n %}
<!DOCTYPE html>
.
.
.
<h1>{% trans "Hello, world!" %}</h1>

```
**Compile Translation Files:** After translating the strings, compile the translation files:
```shell
python manage.py compilemessages
```
**Create Database Tables:** Run the following commands to create the database tables for your app's models after changing you database models in (models.py):
```
python manage.py makemigrations && python manage.py migrate
```


**Run the Development Server:** Start the Django development server to see your multi-language app in action:
```
python manage.py runserver
```

## **--Run django in docker container --**
### Setup :
**Install docker:**
If you haven't installed docker yet, download and install it from the official docker website: https://www.docker.com/.

**Dockerfile:** Create a `Dockerfile` in your project directory with the following content:
```dockerfile

FROM python:3.8 
ENV PYTHONUNBUFFERED 1 
WORKDIR /app COPY requirements.txt /app/ 
RUN pip install --no-cache-dir -r requirements.txt 
COPY . /app/
```
 **requirements.txt:** Create a `requirements.txt` file in your project directory listing the Python dependencies of your Django app.
 ```shell
pip freeze > requirements.txt

```
    
**docker-compose.yml:** Create a `docker-compose.yml` file in your project directory with the following content:
```yaml
version: '3.8'

services:
  db:
    image: mysql:latest
    environment:
      MYSQL_DATABASE: 'your_database_name'
      MYSQL_USER: 'your_mysql_username'
      MYSQL_PASSWORD: 'your_mysql_password'
      MYSQL_ROOT_PASSWORD: 'your_mysql_root_password'
    ports:
      - "3306:3306"

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db

```
**Update Django Settings:** Update your Django project settings (`settings.py`) to use MySQL as the database backend. Replace the `DATABASES` setting with the following:
```yaml
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'db',  # MySQL service name from docker-compose.yml
        'PORT': '3306',
    }
}
```
**Build and Run Docker Container:** Run the following command in your project directory to build and run the Docker container:
```shell
docker-compose up --build

```
**Migrate Database:** after building docker image stop container and run the following command to apply migrations and create tables in the MySQL database:
```shell
docker-compose run web python manage.py migrate

```
**Run the Docker Compose:** Start the Docker containers using Docker Compose:
```
docker-compose up

```
















