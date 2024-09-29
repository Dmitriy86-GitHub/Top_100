from django.db import models


class Actresses(models.Model):
    number = models.IntegerField(blank=True,null=True)
    name = models.CharField(max_length=15, null=True, blank=True)
    name_rus = models.CharField(max_length=15, null=True, blank=True)
    surname = models.CharField(max_length=15, null=True, blank=True)
    surname_rus = models.CharField(max_length=15, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    sign_zodiac = models.CharField(max_length=15, null=True, blank=True)
    city_of_birth = models.CharField(max_length=15, null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    image = models.FileField(null=True, blank=True, upload_to='photos')

    def __str__(self):
        return f'{self.number}{self.name} {self.surname} {self.name_rus} {self.surname_rus} {self.age} {self.date_of_birth} {self.sign_zodiac} {self.city_of_birth} {self.biography}'
