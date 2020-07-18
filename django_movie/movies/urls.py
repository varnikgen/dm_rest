from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = format_suffix_patterns([
    path("movie/", views.MovieViewSet.as_view({'get': 'list'})),  # Список фильмов
    path("movie/<int:pk>/", views.MovieViewSet.as_view({'get': 'retrieve'})),  # Фильм/id
    path("review/", views.ReviewCreateViewSet.as_view({'post': 'create'})),  # Отзыв
    path("rating/", views.AddStarRatingViewSet.as_view({'post': 'create'})),  # Рейтинг
    path("actor/", views.ActorsViewSet.as_view({'get': 'list'})),  # Список актёров
    path("actor/<int:pk>/", views.ActorsViewSet.as_view({'get': 'retrieve'})),  # Список актёров
])
# urlpatterns = [
#     path("movie/", views.MovieListView.as_view()),  # Список фильмов
#     path("movie/<int:pk>/", views.MovieDetailView.as_view()),  # Фильм/id
#     path("review/", views.ReviewCreateView.as_view()),  # Отзыв
#     path("rating/", views.AddStarRatingView.as_view()),  # Рейтинг
#     path("actor/", views.ActorsListView.as_view()),  # Список актёров
#     path("actor/<int:pk>/", views.ActorsDetailView.as_view()),  # Список актёров
# ]
