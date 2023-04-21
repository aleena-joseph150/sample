from django import forms
from .models import *

class studentform(forms.Form):
    sname = forms.CharField(max_length=20)
    dob = forms.DateField()
    phy = forms.FloatField()
    chem = forms.FloatField()
    maths = forms.FloatField()
    cs = forms.FloatField()

