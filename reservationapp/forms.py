import django.forms as forms


class RoomAddForm(forms.Form):
    name = forms.CharField(label='Nazwa sali', max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}))
    capacity = forms.IntegerField(label='Pojemność sali', min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    projector = forms.BooleanField(label='Dostępność rzutnika', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
