# Poll Application

create project using command  
```
django-admin startproject poll_application .
```

created poll app
```
python3 manage.py startapp polls
```

Created model's migrations using below command
```
python3 manage.py makemigrations polls
```

Then added migration
```
python3 manage.py migrate
```

created superuser
```
python3 manage.py createsuperuser
```

run tests of polls app using below command
```
python3 manage.py test polls
```
