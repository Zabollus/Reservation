import django.forms as forms


class RoomAddForm(forms.Form):
    name = forms.CharField(label='Nazwa sali', required=False, max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}))
    capacity = forms.IntegerField(label='Pojemność sali', min_value=0, required=False,
                                  widget=forms.NumberInput(attrs={'class': "form-control"}))
    projector = forms.BooleanField(label='Dostępność rzutnika', required=False,
                                   widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))


class ReservationForm(forms.Form):
    date = forms.DateField(label='Data rezerwacji',
                           widget=forms.DateInput(attrs={'class': "form-control", 'type': 'date'}))
    comment = forms.CharField(label='Komentarz', required=False, widget=forms.Textarea(attrs={'class': "form-control"}))
