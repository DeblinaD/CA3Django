from django.urls import path 
from .import views
urlpatterns=[
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user/',views.user,name='user'),
    path('',views.record,name='record'),
    path('total/',views.total,name='total'),
    path('name/', views.name, name='name'),
    path('visual/', views.visual, name='visual'),
]