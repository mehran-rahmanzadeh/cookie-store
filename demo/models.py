from django.core.validators import RegexValidator
from django.db import models


class User(models.Model):
    """Data model for User
    it will be stored in Session
    no need to migrate this model (just for encapsulation and validation)
    """
    first_name = models.CharField(max_length=50, blank=True, null=True, validators=[RegexValidator(
        regex='^[a-zA-Z]+$', message='Only alphabets are allowed')])
    last_name = models.CharField(max_length=50, blank=True, null=True, validators=[RegexValidator(
        regex='^[a-zA-Z]+$', message='Only alphabets are allowed')])
    phone_number = models.CharField(max_length=20, validators=[RegexValidator(
        regex='^(\+\d{1,3})?,?\s?\d{8,13}', message='Phone number must be valid')])
    email = models.EmailField(blank=True, null=True)
    birth_date = models.DateField()
    mass = models.PositiveIntegerField()
    height = models.PositiveIntegerField()

    def __str__(self):
        return self.phone_number

    def __repr__(self):
        return f'<User {self.phone_number}>'

    class Meta:
        managed = False
