from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('collections',views.collections,name='collections'),
    path('collections/<str:name>',views.collectionview,name='collections'),
    path('collections/<str:cname>/<str:pname>',views.productview,name="collections")
]