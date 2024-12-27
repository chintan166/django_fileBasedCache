django-admin startproject dbcache

cd dbcache/

python3 manage.py startapp cache

python3 manage.py runserver 8041

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py runserver 8042

======================================================================

In settings.py file find middleware and add below code

'django.middleware.cache.UpdateCacheMiddleware', 

'django.middleware.common.CommonMiddleware', 

'django.middleware.cache.FetchFromCacheMiddleware',

------------------------------=====

in last of settings.py file add below code

CACHE_MIDDLEWARE_SECONDS = 10
CACHES = {
    'default': {
        'BACKEND':'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION':'/var/www/html/dj_cache_db/dbcache/cache_files',
    }
}

---------------------------------------------------------------------

you can see the cache in below images like in "cache_files" folder 

![Screenshot from 2024-12-27 16-16-06](https://github.com/user-attachments/assets/4408da98-bbd1-418d-b795-069d65c47ebb)

