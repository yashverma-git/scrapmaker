from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('features/', views.features, name='features'),
    path('buy/', views.buy, name='buy'),
    path('sell/', views.sell, name='sell'),
    path('offer/', views.offer, name='offer'),
]
