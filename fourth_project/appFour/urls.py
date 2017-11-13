from django.conf.urls import url, include
from appFour import views

app_name = 'appFour'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
]
