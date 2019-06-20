from webapp.models import User, Name, Location, Coordinates, TimeZone, Login, Dob, Registered, Picture, Id
from rest_framework import serializers


class InlineNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = ('title', 'first', 'last')


class InlineCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = ('latitude', 'longitude')


class InlineTimeZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeZone
        fields = ('offset', 'description')


class InlineLocationSerializer(serializers.ModelSerializer):
    coordinates = InlineCoordinatesSerializer(read_only=True)
    timezone = InlineTimeZoneSerializer(read_only=True)

    class Meta:
        model = Location
        fields = ('street', 'city', 'state', 'postcode', 'coordinates', 'timezone')


class InlineLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('uuid', 'username', 'password', 'salt', 'md5', 'sha1', 'sha256')


class InlineDobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dob
        fields = ('date', 'age')


class InlineRegisteredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registered
        fields = ('date', 'age')


class InlineIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Id
        fields = ('name', 'value')


class InlinePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('large', 'medium', 'thumbnail')


class UserSerializer(serializers.ModelSerializer):
    name = InlineNameSerializer(read_only=True)
    location = InlineLocationSerializer(read_only=True)
    login = InlineLoginSerializer(read_only=True)
    dob = InlineDobSerializer(read_only=True)
    registered = InlineRegisteredSerializer(read_only=True)
    user_id = InlineIdSerializer(read_only=True)
    picture = InlinePictureSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('gender', 'name', 'location', 'email', 'login', 'dob',
                  'registered', 'phone', 'cell', 'user_id', 'picture', 'nat')


class ShortUserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    country_code = serializers.CharField(max_length=3)



class NumbersFromHashSerialaizer(serializers.Serializer):
    md5 = serializers.CharField(max_length=255)
    sha1 = serializers.CharField(max_length=255)
    sha256 = serializers.CharField(max_length=255)