from django import forms
from django.core import validators
import datetime
# from .models import MyModel


# widgets == field to html input
class contactForm(forms.Form):
    name = forms.CharField(label="Full Name : ", help_text="Total length must be within 70 characters", required=False, error_messages={'required': 'Please enter your name.'},widget = forms.Textarea(attrs = {'id' : 'text_area', 'class' : 'class1 class 2', 'placeholder' : 'Enter your name'},))
    

    #comment = forms.CharField(widget=forms.Textarea)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))

    #email = forms.EmailField()
    email = forms.EmailField(label = "User Email")

    #agree = forms.BooleanField()
    agree = forms.BooleanField(initial=True)
    day = forms.DateField(initial=datetime.date.today)
    date = forms.DateField()
    birth_date = forms.DateField(widget=forms.DateInput(attrs= {'type' : 'date'}))

    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    value = forms.DecimalField()
    email_address = forms.EmailField( required = False,)
    message = forms.CharField(max_length = 10,)
    email_address = forms.EmailField( label="Please enter your email address",)
    first_name = forms.CharField(initial='Your name')
    
    

    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    #favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    #favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)
   
    
    # model_choices = forms.ModelMultipleChoiceField(
    #     widget = forms.CheckboxSelectMultiple,
    #     queryset = MyModel.objects.all(),
    #     initial = 0
    #     )
    

    first_name = forms.CharField(max_length = 200)  
    last_name = forms.CharField(max_length = 200)  
    roll_number = forms.IntegerField(  
                     help_text = "Enter 6 digit roll number"
                     )  
    password = forms.CharField(widget = forms.PasswordInput())






   








