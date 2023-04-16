from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('debate/<slug:page_slug>/', show_page, name='debate'),
    path('category/<int:cat_id>/', show_category, name='category'),
]