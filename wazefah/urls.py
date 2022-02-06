from django.urls import URLPattern, path
from . import views

app_name = 'wazefah'

urlpatterns = [
    path('',views.BaseView.as_view(), name='base'),
    path('home/',views.HomeView.as_view(), name='home'),
]