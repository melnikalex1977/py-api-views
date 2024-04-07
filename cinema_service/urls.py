from django.contrib import admin
from django.urls import path, include

from cinema.views import (
    GenreList,
    GenreDetail,
    movie_list,
    movie_detail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet
)


cinema_hall_list = (
    CinemaHallViewSet.as_view(
        actions={"get": "list", "post": "create"}
    )
)
cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/cinema/", include("cinema.urls", namespace="cinema")),
    path("genres/", GenreList.as_view(), name="genre_list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre_detail"),
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie_detail"),
    path("cinema_halls/", cinema_hall_list, name="cinema_hall_list"),
    path(
        "cinema_halls/<int:pk>/",
        cinema_hall_detail,
        name="cinema_hall_detail"
    ),
    path("actors/", ActorList.as_view(), name="actor_list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),
]
app_name = "cinema"
