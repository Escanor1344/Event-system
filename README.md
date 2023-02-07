## About The Project
___

Event management system that receives POST requests in the format:
``` commandline
{
"event_type": <event_type.name>,
"info": <any json>,
"timestamp": <datetime>
}
```

This data is stored in two models:
``` python
class EventType(models.Model):
    name = models.CharField(max_length=256, unique=True)


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, auto_created=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    info = models.JSONField()
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)
```
If **event_type.name** which receive not in db ---> add it and create new data
with it.
## How to run the project?
___

1. ``` git clone https://github.com/Escanor1344/Event-system.git ```
2. ``` pip install django ```
3. ``` pip install djangorestframework ```
4. ``` pip install requests ```
5. ``` python manage.py createsuperuser ```
6. ``` python manage.py drf_create_token 'user' ```.
Other than getting a token via 'manage.py' it can be done by url. send request to url 'http://127.0.0.1/token'
to get a token. 
Example with requests:
```python
import requests

url = 'http://127.0.0.1:8000/token/'

r = requests.post(url, data={
  'username': 'user',
  'password': 'user_password'
  }
)
```

7. ``` python manage.py runserver ```


### Built With
+ <img src="https://img.shields.io/badge/Python-black?style=for-the-badge&logo=Python"/>
+ <img src="https://img.shields.io/badge/Django-black?style=for-the-badge&logo=Django&logoColor=green"/>
+ <img src="https://img.shields.io/badge/Django REST Framework-black?style=for-the-badge&logo=Django&logoColor=red"/>
+ <img src="https://img.shields.io/badge/SQLite-black?style=for-the-badge&logo=SQLite&logoColor=grey"/>