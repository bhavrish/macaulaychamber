from django.urls import path

from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>', views.detail, name='detail'), # take blog number in URL and store to blog_id
]