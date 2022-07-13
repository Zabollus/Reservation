"""Reservation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reservationapp.views import RoomAddView, RoomListView, RoomDeleteView, RoomModifyView, ReservationView, RoomDetailsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RoomListView.as_view(), name='rooms'),
    path('room/new', RoomAddView.as_view(), name='room-add'),
    path('room/delete/<int:room_id>', RoomDeleteView.as_view(), name='room-delete'),
    path('room/modify/<int:room_id>', RoomModifyView.as_view(), name='room-modify'),
    path('room/reserve/<int:room_id>', ReservationView.as_view(), name='room-reserve'),
    path('room/<int:room_id>', RoomDetailsView.as_view(), name='room')
]
