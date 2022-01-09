# Local APP
This is the localstore app, in which user can add the locational information 
 and the location information will be shown in the local/list url and the details local/value

## Getting Started/Installing

```
pip install -r requirements.txt
```
Make sure to change the database connection parameters from latlongproject/settings.py file:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        
    }
}
```
to apply database 
```
python manage.py migrate

```
to start the server.
```
python manage.py runserver

```
## To run the tests
```
python manage.py test
```
To add a local is necessary to copy the lat and lot from the marker popup in the fields in the form
## Frameworks :
* Django  

## Database:
* Postgresql
