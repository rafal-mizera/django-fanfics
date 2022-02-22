from django.urls import path
from . import views

app_name = 'fanfics'

urlpatterns = [
    path('home/',views.home, name='home'),
    path('new_publication/',views.new_publication, name='new_publication'),
    path('new/', views.publications, name='publications'),
    path('<int:year>/<int:month>/<int:day>/<slug:publication>/',views.publication_details,name='publication_details'),
    path('tag/<slug:tag_slug>/',views.publications, name='publications_by_tag'),
    path('<name>',views.publications_by_user, name='publications_by_user'),
    path('like/', views.publication_like, name='publication_like'),
    path('best_publications/',views.best_publications, name='best_publications'),
]