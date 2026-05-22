from django.urls import path,include
from django.contrib import admin
from . import views


urlpatterns = [
    #  path('admin/', admin.site.urls),
    path("", views.room, name="room"),
    path("<str:slug>",views.room_view,name="room_view")
]

