from django.urls import path
from . import views

urlpatterns = [
    path('', views.single_profile_search, name='single_search'),
    path('single-result', views.single_profile_detail, name='single_result'),
    path('dual-search', views.dual_profile_search, name='dual_search'),
    path('dual-result', views.dual_profile_detail, name='dual_result')
]
