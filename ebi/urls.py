from django.urls import path
from . import views

urlpatterns = [
    #Leave as empty string for base url
    path('', views.ebi, name='ebi'),
    path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

]