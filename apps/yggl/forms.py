from django import forms

from .models import Yg, YgCategory


class YgForm(forms.ModelForm):
    class Meta:
        model = Yg
        fields = "__all__"
        exclude=['clicknum', 'favornum', 'commtnum', 'created_at', 'updated_at']


class YgCategoryForm(forms.ModelForm):
    class Meta:
        model = YgCategory
        fields = "__all__"
        exclude=['user', 'clicknum', 'favornum', 'commtnum', 'created_at', 'updated_at']
