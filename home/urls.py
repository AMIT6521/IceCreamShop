
from django.contrib import admin
from django.urls import path
from home import views


admin.site.site_header = "IceCreams Admin"
admin.site.site_title = "IceCreams Admin Portal"
admin.site.index_title = "Welcome to IceCream Shop "

urlpatterns = [
    path ('admin/', admin.site.urls), 

    path('', views.index, name='home'),

    path('about', views.about, name='about'),

    path('menu', views.menu, name='menu'),

    path('contact', views.contact, name='contact'),

]
