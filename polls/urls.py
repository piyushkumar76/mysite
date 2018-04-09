from django.urls import path
from . import views


urlpatterns = [
    # ex: /polls/
    #path('', views.index, name='index'),
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('police/', views.savePolice),
    path('police/',views.PoliceListEntry),
    path('station/',views.policeStation),
    path('UserRequest/',views.UserRequest),
    path('getpolice/',views.PoliceEntrys.as_view()),
    path('getstation/',views.StationsList.as_view()),
    path('Request/',views.UserList.as_view()),
]
