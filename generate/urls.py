from django.urls import path
from .views import generate_code,hi,result

urlpatterns = [
    path('generate_code/', generate_code, name='generate_code'),
    path('result/', result, name='result'),
    
    
]
