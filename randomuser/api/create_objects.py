from webapp.models import User, Picture, Name, Coordinates, TimeZone, Location, Login, Id, Registered, Dob
from api.handling import generate_email, convert_string


def create_name(results):
    return Name.objects.create(title=results['name']['title'],
                               first=results['name']['first'],
                               last=results['name']['last'])


def create_coordinates(coordinates):
    return Coordinates.objects.create(latitude=coordinates['latitude'],
                                      longitude=coordinates['longitude'])


def create_timezone(timezone):
    return TimeZone.objects.create(offset=timezone['offset'],
                                   description=timezone['description'])


def create_location(results):
    return Location.objects.create(street=results['location']['street'],
                                   city=results['location']['city'],
                                   state=results['location']['state'],
                                   postcode=results['location']['postcode'],
                                   coordinates=create_coordinates(results['location']['coordinates']),
                                   timezone=create_timezone(results['location']['timezone']))


def create_login(results):
    return Login.objects.create(uuid=results['login']['uuid'],
                                username=results['login']['username'],
                                password=results['login']['password'],
                                salt=results['login']['salt'],
                                md5=convert_string(results['login']['md5']),
                                sha1=convert_string(results['login']['sha1']),
                                sha256=convert_string(results['login']['sha256']))


def create_dob(results):
    return Dob.objects.create(date=results['dob']['date'],
                              age=results['dob']['age'])


def create_registered(results):
    return Registered.objects.create(date=results['registered']['date'],
                                     age=results['registered']['age'])


def create_id(results):
    return Id.objects.create(name=results['id']['name'],
                             value=results['id']['value'])


def create_picture(results):
    return Picture.objects.create(large=results['picture']['large'],
                                  medium=results['picture']['medium'],
                                  thumbnail=results['picture']['thumbnail'])


def create_user(results):
    gender = results['gender']
    phone = results['phone']
    cell = results['cell']
    nat = results['nat']
    email = generate_email(results)
    picture = create_picture(results)
    user_id = create_id(results)
    dob = create_dob(results)
    registered = create_registered(results)
    name = create_name(results)
    login = create_login(results)
    location = create_location(results)
    return User.objects.create(name=name, gender=gender, location=location, email=email, phone=phone, cell=cell,
                               nat=nat, picture=picture, user_id=user_id, dob=dob, registered=registered, login=login)
