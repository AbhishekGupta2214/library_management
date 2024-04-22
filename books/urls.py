from django.urls import  path
from . import views
urlpatterns = [
    path('',views.Index,name='index'),
    path('book',views.BookGet,),
    path('bookshow/',views.Details),
    path('search',views.Search,name='Search-form'),
]