A simple todo app built with django


![[2024-03-20_03-50.png]]

### Setup
        

 setup django , run this command 
```bash
python -m pip install Django==5.0.3
```
setup virtual enviorement for python project

```shell
pipenv shell

```
install the dependencies needed for the project
```shell
cd /todov
pip install -r requirements.txt
```
create MySQL work environment 
```shell
pip install mysql

pip install mysql-connector

pip install mysql-connector-python
```
modifier file todov/database.py with your database settings, then this command
```shell
python database.py
```


```bash
$ python manage.py makemigrations
```

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command
```bash
$ python manage.py migrate
```

Start the server by following command

```bash
$ python manage.py runserver
```

Once the server is hosted, head over to http://127.0.0.1:8000/todos for the App.


