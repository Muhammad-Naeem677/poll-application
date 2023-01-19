from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
  # ex: /polls/
  path('', views.IndexView.as_view(), name='index'),
  # ex: /polls/:id/
  path('<int:pk>/', views.DetailView.as_view(), name='detail'),
  # ex: /polls/:id/results/
  path('<int:pk>/results', views.ResultsView.as_view(), name='results'),
  # ex: /polls/:id/vote/
  path('<int:question_id>/vote', views.vote, name='vote'),
]
