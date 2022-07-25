from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import *


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class ProductForm(ModelForm):

    class Meta:
        model = ProductDetails
        fields = '__all__'
        
