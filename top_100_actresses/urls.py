from django.urls import path
from .views import show_all_actresses, CreateActressView, done, UpdateActressView, ActressDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', show_all_actresses,name=''),
    path('actress/<int:pk>',ActressDetailView.as_view(),name='actress'),
    path('actress_form', CreateActressView.as_view(), name='actress_form'),
    path('done', done),
    path('<int:pk>', UpdateActressView.as_view()),

    # path('actress', views.show_one_actress),
]
