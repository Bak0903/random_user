from django.urls import include, path
from api import views

app_name = 'api'

urlpatterns = [
    path('user', views.random_user),
    path('user_short', views.random_user_short),
    path('hash_numbers', views.numbers_from_hash),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]