from vehicle.models import Vehicle
from .models import Agency
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# PROFILE FORMS
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileForm(ModelForm):
    class Meta:
        model=Agency
        fields = ['image','name', 'bio','contact_phone', 'contact_email', 'contact_website', 'state', 'city', 'address']

# VEHCILE FORMS
class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['year', 'type', 'price','engine', 'transmission', 'color', 'seats', 'doors', 'mileage', 'description'] 
