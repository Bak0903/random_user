import re


def convert_string(string):
    result = ''.join(let for let in re.findall(r'[\D]', string))
    result += ''.join(let for let in re.findall(r'[\d]', string))
    return result


def get_numbers(string):
    email = ''.join(let for let in re.findall(r'[\d]', string))
    email.replace(" ", "")
    return email


def generate_email(results):
    return "%s%s@%s.%s" % (results['name']['first'],
                           results['name']['last'],
                           results['location']['city'],
                           results['nat'].lower())
