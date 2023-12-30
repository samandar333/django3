from django.urls import path
from .views import HomepageView, AboutpageView, indexpageView

urlpatterns = [
    path('about/', AboutpageView.as_view(), name='about'),
    path('', HomepageView.as_view(), name='home'),
    path('index', indexpageView.as_view(), name='index')
]