from django import forms
from .models import Actresses

# class GalleryUploadForm(forms.Form):
#     photo = forms.FileField()
class ActressesForm(forms.ModelForm):
    class Meta:
        model = Actresses
        fields = '__all__'
        labels = {
            'name_rus': 'Имя',
            'number': 'Номер',
            'surname_rus': 'Фамилия',
            'age': 'Возраст',
            'date_of_birth': 'Дата рождения',
            'sign_zodiac': 'Знак зодиака',
            'city_of_birth': 'Место рождения',
            'biography': 'Биография',
            'image': 'Изображение'

        }
