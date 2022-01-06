from django.urls import path
from .views import (
    LocalListView,
    LocalDetailView,
    LocalUpdateView,
    LocalCreateView,
    LocalDeleteView,
    SearchResultsListView,
    HomePageView,
)

urlpatterns = [
    path('local/list', LocalListView.as_view(), name='local_list'),
    path('local/<int:pk>/',LocalDetailView.as_view(), name='local_detail'),
    path('local/<int:pk>/update/',LocalUpdateView.as_view(), name='local_update'),
    path('local/add/',LocalCreateView.as_view(), name='add_local'),
    path('local/<int:pk>/del',LocalDeleteView.as_view(), name='local_delete'),
    path('local/search/', SearchResultsListView.as_view(), name='search_results'),
    path('local',HomePageView.as_view(), name='home'),
]
