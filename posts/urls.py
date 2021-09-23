from django.urls import path
from .views import PostListView, PostView


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('posts/<int:pk>/', PostView.as_view(), name='post_detail'),
]
