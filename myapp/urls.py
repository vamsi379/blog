from django.urls import path
from myapp.views import index,detail

app_name = 'myapp'

urlpatterns = [
    path('',index,name = 'index'),
    path('<int:pk>/',detail,name = 'detail'),
]