from django.db import models


class User(models.Model):
    gender = models.CharField(max_length=15)
    name = models.OneToOneField('Name', on_delete=models.CASCADE)
    location = models.OneToOneField('Location', on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    dob = models.OneToOneField('Dob', on_delete=models.CASCADE)
    registered = models.OneToOneField('Registered', on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)
    cell = models.CharField(max_length=255)
    user_id = models.OneToOneField('Id', on_delete=models.CASCADE)
    picture = models.OneToOneField('Picture', on_delete=models.CASCADE)
    nat = models.CharField(max_length=3)
    login = models.ForeignKey('Login', on_delete=models.CASCADE)


class Name(models.Model):
    title = models.CharField(max_length=255)
    first = models.CharField(max_length=255)
    last = models.CharField(max_length=255)


class Location(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postcode = models.IntegerField()
    coordinates = models.OneToOneField('Coordinates', on_delete=models.CASCADE)
    timezone = models.ForeignKey('TimeZone', on_delete=models.CASCADE)


class Coordinates(models.Model):
    latitude = models.CharField(max_length=8)
    longitude = models.CharField(max_length=8)


class TimeZone(models.Model):
    offset = models.CharField(max_length=5)
    description = models.CharField(max_length=255)


class Login(models.Model):
    uuid = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    salt = models.CharField(max_length=255)
    md5 = models.CharField(max_length=255)
    sha1 = models.CharField(max_length=255)
    sha256 = models.CharField(max_length=255)


class Dob(models.Model):
    date = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()


class Registered(models.Model):
    date = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()


class Id(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255, blank=True, null=True)


class Picture(models.Model):
    large = models.CharField(max_length=255)
    medium = models.CharField(max_length=255)
    thumbnail = models.CharField(max_length=255)
