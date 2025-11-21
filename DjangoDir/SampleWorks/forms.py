from django import forms
from django.forms import ModelForm
from SampleWorks.models import College

class ApplicationForm(forms.Form):
    name = forms.CharField(label="Applicant name", max_length=50)
    addr = forms.CharField(label="Address", max_length=100)
    posts = (
        ("Manager", "Manager"),
        ("Cashier", "Cashier"),
        ("Operator", "Operator"),
    )
    age_groups = (
        ("1", "20-30"),
        ("2", "30-40"),
        ("3", "40-50"),
    )
    role = forms.ChoiceField(choices=posts)
    age_group = forms.ChoiceField(choices=age_groups)


class createCollege(ModelForm):
    class Meta:
        model = College
        # fields = "__all__"
        fields = ['name', 'age', 'website']


