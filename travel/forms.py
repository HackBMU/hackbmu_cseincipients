from django import forms
from django.contrib.auth.models import User
from travel.models import UserProfile, user_services

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, help_text="Username",
                               widget=forms.TextInput(attrs={'class': 'validate', 'input': 'text'}))
    password = forms.CharField(widget=forms.PasswordInput(), required=True, help_text="Password")
    email = forms.EmailField(max_length=100, required=True, help_text="Email",
                             widget=forms.EmailInput(attrs={'class': 'validate', 'input': 'email'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    name = forms.CharField(max_length=30, required=True, help_text="Name",
                           widget=forms.TextInput(attrs={'class': 'validate', 'input': 'text'}))
    contact = forms.CharField(required=True, help_text="Phone Number",
                              widget=forms.TextInput(attrs={'class': 'validate', 'input': 'text', 'maxlength': '10'}))
    college = forms.CharField(max_length=100, required=True, help_text="College Name",
                              widget=forms.TextInput(attrs={'class': 'validate', 'input': 'text'}))
    gender = forms.ChoiceField(choices=[('0', 'Female'), ('1', 'Male'), ('2', 'Other')])
    picture = forms.ImageField(help_text='Profile Picture', required=False,
                               widget=forms.FileInput(attrs={'type': 'file'}))
    location = forms.ChoiceField(choices=[('Gurgaon','Gurgaon'),('Kapriwas','Kapriwas'),('Manesar','Manesar')])
    aadhar_no =forms.CharField(max_length=12, required=True, help_text="Aadhar Number",
                               widget=forms.TextInput(attrs={'class': 'validate', 'input': 'text'}))

    class Meta:
        model = UserProfile
        fields = ('name', 'contact', 'college', 'gender', 'picture', 'location', 'aadhar_no')

class TripPlannerForm(forms.ModelForm):
    source = forms.CharField(max_length=30, required=True,
                             help_text="Source (Options are : BML, Manesar, Rajiv Chowk, Iffco Chowk)",
                           widget=forms.TextInput(attrs={'class': 'validate', 'input': 'text'}))
    destination = forms.CharField(max_length=30, required=True,
                                  help_text="Destination (Options are : BML, Manesar, Rajiv Chowk, Iffco Chowk)",
                           widget=forms.TextInput(attrs={'class': 'validate', 'input': 'text'}))
    date = forms.CharField(max_length=30, required=True,
                           help_text="Date (Format is DD/MM/YYYY)",
                           widget=forms.TextInput(attrs={'class': 'validate', 'input': 'text'}))
    time = forms.CharField(max_length=30, required=True,
                           help_text="Time (Format is HH:MM AM/PM)",
                           widget=forms.TextInput(attrs={'class': 'validate', 'input': 'text'}))
    seats_need = forms.IntegerField(help_text="Number of seats")

    class Meta:
        model = user_services
        fields = ('source', 'destination', 'date', 'time', 'seats_need')