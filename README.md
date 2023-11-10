## 1. Install dependencies
```
pip install -r requirements.txt
```

## 2. Models migrate
```
py manage.py migrate
or
python manage.py migrate
```

## 3. Generate demo data
```
py manage.py demo_blog
or
python manage.py demo_blog
```

## 4. Run redis in docker
```
docker run -p 6379:6379 redis
```

## 5. Run Django web server
```
py manage.py runserver
or
python manage.py runserver
```