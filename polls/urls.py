from django.urls import path

from . import views

urlpatterns = [
  # ex: /polls/
  path('', views.index, name='index'),
  # ex: /polls/:id/
  path('<int:question_id>/', views.detail, name='detail'),
  # ex: /polls/:id/results/
  path('<int:question_id>/', views.results, name='results'),
  # ex: /polls/:id/vote/
  path('<int:question_id>/', views.vote, name='vote'),
]
