# from django.urls import path
from . import views
from django.urls import path
from .views import PostListView
# urlpatterns = [
#     path('', views.post_list, name='home'),

# ]


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
]
