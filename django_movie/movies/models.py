from django.db import models
from datetime import date

from django.urls import reverse


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Actor(models.Model):
    """Актёры и режисcёры"""
    name = models.CharField("Именя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actors/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actor_detail', kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Актёры и режисcёры"
        verbose_name_plural = "Актёры и режисcёры"


class Genre(models.Model):
    """Жанр"""
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Movie(models.Model):
    """Фильмы"""
    title = models.CharField("Название", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2020)
    country = models.CharField("Страна", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="режиссёр", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="актёры", related_name="film_actor")
    genre = models.ManyToManyField(Genre, verbose_name="жанры")
    world_premiere = models.DateField("Премьера в мире", default=date.today)
    budget = models.PositiveIntegerField("Бюджет", default=0, help_text="указывать сумму в рублях")
    fees_in_usa = models.PositiveIntegerField("Сборы в США", default=0, help_text="указывать сумму в рублях")
    fees_in_world = models.PositiveIntegerField("Сборы в мире", default=0, help_text="указывать сумму в рублях")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class MovieShots(models.Model):
    """Кадры из фильма"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из Фильма"
        verbose_name_plural = "Кадры из Фильма"


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.PositiveSmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звёзды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP-адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE, related_name="ratings")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Review(models.Model):
    """Отзыв"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Собщение", max_length=5000)
    parent = models.ForeignKey(
        "self", verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True, related_name="children"
    )
    movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
