from django.urls import path

from . import views

urlpatterns = [
    path("movie/", views.MovieListView.as_view()),  # Список фильмов
    path("movie/<int:pk>/", views.MovieDetailView.as_view()),  # Фильм/id
    path("review/", views.ReviewCreateView.as_view()),  # Отзыв
    path("rating/", views.AddStarRatingView.as_view()),  # Рейтинг
    path("actors/", views.ActorsListView.as_view()),  # Список актёров
    path("actors/<int:pk>/", views.ActorsDetailView.as_view()),  # Список актёров
]
