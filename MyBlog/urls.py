from django.urls import path
from .views import (
    IndexView,
    DetailView,
    CreatePostView,
    HotelView,
    RestaurantView,
    UpdatePostView,
    DeletePostView,
    InterviewView,
    LikeView,
)


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("artykuł/<int:pk>", DetailView.as_view(), name="details"),
    path("utwórz/", CreatePostView.as_view(), name="create"),
    path("hotelarstwo/", HotelView.as_view(), name="hotel"),
    path("restauracje/", RestaurantView.as_view(), name="restaurant"),
    path("wywiady/", InterviewView.as_view(), name="interview"),
    path("artykuł/edycja/<int:pk>", UpdatePostView.as_view(), name="update"),
    path("artykuł/<int:pk>/usuń", DeletePostView.as_view(), name="delete"),
    path("like/<int:pk>", LikeView, name="like_post"),
    # path("kategorie/", CategoryView.as_view(), name="categories"),
]
