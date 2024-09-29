from django.urls import path
from .views import index,sign_zodiac

urlpatterns = [
    path('horoscope', index, name='horoscope'),
    path('horoscope/<str:sign>', sign_zodiac, name='sign_zodiac'),

]
