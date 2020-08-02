from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from booking.models import Hotel

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class StaffForm(ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'
        labels = {'name':'Hotel Name','desc':'Description'}