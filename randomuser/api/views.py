from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import UserSerializer, ShortUserSerializer, NumbersFromHashSerialaizer
from api.get_request import RandomUserShort, NumbersFromHash, get_random_user
from api.create_objects import create_user


@api_view()
def random_user(request):
    data = get_random_user()
    user = create_user(data)
    json = UserSerializer(user)
    return Response(json.data)


@api_view()
def random_user_short(request):
    user = RandomUserShort()
    json = ShortUserSerializer(user)
    return Response(json.data)


@api_view()
def numbers_from_hash(request):
    hashes = NumbersFromHash()
    json = NumbersFromHashSerialaizer(hashes)
    return Response(json.data)
