import requests
from api.handling import generate_email, get_numbers


def get_random_user():
    response = requests.get('https://randomuser.me/api/')
    data = response.json()
    results = data['results'][0]
    return results


class RandomUserShort(object):
    def __init__(self):
        resp = requests.get('https://randomuser.me/api/?inc=location,name,nat&noinfo')
        data = resp.json()
        results = data['results'][0]
        self.first_name = results['name']['first']
        self.last_name = results['name']['last']
        self.email = generate_email(results)
        self.city = results['location']['city']
        self.country_code = results['nat']


class NumbersFromHash(object):
    def __init__(self):
        resp = requests.get('https://randomuser.me/api/?inc=login&noinfo')
        data = resp.json()
        results = data['results'][0]
        self.md5 = get_numbers(results['login']['md5'])
        self.sha1 = get_numbers(results['login']['sha1'])
        self.sha256 = get_numbers(results['login']['sha256'])
