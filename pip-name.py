"""Check whether a package name is available on PyPi"""

import argparse
import requests

BASE_URL = 'https://pypi.org/pypi'


def get_response(name):
    target_url = '{0}/{1}/json'.format(BASE_URL, name)
    r = requests.get(target_url)
    
    # todo handle exceptions
    return r.json()


def is_name_taken(name):
    response = get_response(name)

    if response == '404':
        return False

    file_name = response.get('urls')[0].get('filename').split('-')[0]

    # check filename of the found package
    if name == file_name:
        return True
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='name of the package you want to check', type=str)
    args = parser.parse_args()

    if is_name_taken(args.name):
        print('`{0}` is unavailable.'.format(args.name))
    else:
        print('{0} is available'.format(args.name))

if __name__ == '__main__':
    main()
