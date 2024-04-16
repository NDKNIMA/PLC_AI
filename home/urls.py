from .views import hi,about
from django.urls import path
urlpatterns = [
    
    path('', hi, name='HOME'),
    path('About/', about, name='About'),
    

]
