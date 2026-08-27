from django.urls import path
from . import views
from . import newrouter
urlpatterns=[
    path('',views.rodrigo,name='rodrigo'),
    path('index/',newrouter.index2,name='index')
    
    
]