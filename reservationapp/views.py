from django.shortcuts import render, redirect
from django.views import View
from reservationapp.models import Room, Reservation
from reservationapp.forms import RoomAddForm, ReservationForm
import datetime
# Create your views here.


class RoomAddView(View):
    def get(self, request):
        form = RoomAddForm()
        title = "Dodaj salę"
        return render(request, 'form.html', {'form': form, 'title': title})

    def post(self, request):
        form = RoomAddForm(request.POST)
        title = "Dodaj salę"
        if form.is_valid():
            name = form.cleaned_data['name']
            capacity = form.cleaned_data['capacity']
            projector = form.cleaned_data['projector']
            error = ''
            if not name:
                error = 'Nie podano nazwy sali'
            if capacity <= 0:
                error = 'Pojemność sali musi być dodatnia'
            if Room.objects.filter(name=name).first():
                error = 'Sala o podanej nazwie już istnieje'
            if error:
                return render(request, 'form.html', {'form': form, 'title': title, 'error': error})
            Room.objects.create(name=name, capacity=capacity, projector_availability=projector)
            return redirect('/')


class RoomListView(View):
    def get(self, request):
        rooms = Room.objects.all().order_by('id')
        for room in rooms:
            reservation_dates = [reservation.date for reservation in room.reservation_set.all()]
            room.reserved = datetime.date.today() in reservation_dates
        form = RoomAddForm()
        return render(request, 'rooms.html', {'rooms': rooms, 'form': form})


class RoomDeleteView(View):
    def get(self, request, room_id):
        room = Room.objects.get(id=room_id)
        room.delete()
        return redirect('rooms')


class RoomModifyView(View):
    def get(self, request, room_id):
        room = Room.objects.get(id=room_id)
        title = 'Edytuj salę'
        form = RoomAddForm(initial={
            'name': room.name,
            'capacity': room.capacity,
            'projector': room.projector_availability
        })
        return render(request, 'form.html', {'form': form, 'title': title})

    def post(self, request, room_id):
        room = Room.objects.get(id=room_id)
        title = 'Edytuj salę'
        form = RoomAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            capacity = form.cleaned_data['capacity']
            projector = form.cleaned_data['projector']
            error = ''
            if capacity <= 0:
                error = 'Pojemność sali musi być dodatnia'
            if name != room.name and Room.objects.filter(name=name).first():
                error = 'Sala o podanej nazwie już istnieje'
            if error:
                return render(request, 'form.html', {'form': form, 'title': title, 'error': error})
            room.name = name
            room.capacity = capacity
            room.projector_availability = projector
            room.save()
            return redirect('/')


class ReservationView(View):
    def get(self, request, room_id):
        room = Room.objects.get(id=room_id)
        form = ReservationForm()
        title = 'Zarezerwuj salę'
        reservations = room.reservation_set.filter(date__gte=str(datetime.date.today())).order_by('date')
        return render(request, 'form.html', {'form': form, 'title': title, 'room': room, 'reservations': reservations})

    def post(self, request, room_id):
        room = Room.objects.get(id=room_id)
        form = ReservationForm(request.POST)
        title = 'Zarezerwuj salę'
        reservations = room.reservation_set.filter(date__gte=str(datetime.date.today())).order_by('date')
        if form.is_valid():
            date = form.cleaned_data['date']
            comment = form.cleaned_data['comment']
            error = ''
            if Reservation.objects.filter(room=room, date=date):
                error = 'Sala jest już zarezerwowana w tym terminie!'
            if str(date) < str(datetime.date.today()):
                error = 'Data jest z przeszłości!'
            if error:
                return render(request, 'form.html', {'form': form, 'title': title, 'room': room,
                                                     'reservations': reservations, 'error': error})
            Reservation.objects.create(room=room, date=date, comment=comment)
            return redirect('rooms')


class RoomDetailsView(View):
    def get(self, request, room_id):
        room = Room.objects.get(id=room_id)
        reservations = room.reservation_set.filter(date__gte=str(datetime.date.today())).order_by('date')
        return render(request, 'room_details.html', {'room': room, 'reservations': reservations})


class SearchView(View):
    def post(self, request):
        form = RoomAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            capacity = form.cleaned_data['capacity']
            projector = form.cleaned_data['projector']
            rooms = Room.objects.all().order_by('id')
            if projector:
                rooms = rooms.filter(projector_availability=projector)
            if capacity:
                rooms = rooms.filter(capacity__gte=capacity)
            if name:
                rooms = rooms.filter(name__contains=name)

            for room in rooms:
                reservation_dates = [reservation.date for reservation in room.reservation_set.all()]
                room.reserved = datetime.date.today() in reservation_dates

            return render(request, 'rooms.html', {'rooms': rooms, 'form': form})
