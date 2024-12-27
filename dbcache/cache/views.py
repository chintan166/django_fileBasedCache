from django.shortcuts import render
from django.db import connections
from django.core.cache import cache



def home(request):
    data = cache.get('my_key')
    if data is None:
        # If not cached, compute the value and store it in the cache
        data = "This is cached data"
        cache.set('my_key', data, timeout=30)
        
    return render(request,'cache/course.html')
