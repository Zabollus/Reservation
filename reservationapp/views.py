from django.shortcuts import render, redirect
from django.views import View
from reservationapp.models import Room
from reservationapp.forms import RoomAddForm

# Create your views here.


class LandingPageView(View):
    def get(self, request):
        return render(request, 'base.html')


class RoomAddView(View):
    def get(self, request):
        form = RoomAddForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = RoomAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            capacity = form.cleaned_data['capacity']
            projector = form.cleaned_data['projector']
            error = ''
            if capacity <= 0:
                error = 'Pojemność sali musi być dodatnia'
            if Room.objects.filter(name=name).first():
                error = 'Sala o podanej nazwie już istnieje'
            if error:
                return render(request, 'form.html', {'form': form, 'error': error})
            Room.objects.create(name=name, capacity=capacity, projector_availability=projector)
            return redirect('/')

