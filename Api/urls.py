from django.urls  import path
from .import views

urlpatterns = [
    path('api/',views.Get_View),
    path('',views.home_view ,name = 'home')

]