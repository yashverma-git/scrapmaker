from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),          # Home page
    path('about/', views.about, name='about'),   # About page
    path('contact/', views.contact, name='contact'), # Contact page
    path('features/', views.features, name='features'), # Features page
    path('buy/', views.buy, name='buy'),          # Buy page
    path('sell/', views.sell, name='sell'),        # Sell page
    path('offer/', views.offer, name='offer'),   # Offer page
]
