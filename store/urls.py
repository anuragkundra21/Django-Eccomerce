from django.urls import path
from store import views
urlpatterns = [
    path("",views.index,name='index'),
    path("about/",views.about,name='About'),
    path("search/",views.search,name='Search'),
    path("product/<int:myid>",views.product,name='Product Details'),
    path("register/",views.register,name='Register'),
    path("login/",views.login,name='Login'),
    path("checkout/",views.checkout,name='Checkout'),
]
