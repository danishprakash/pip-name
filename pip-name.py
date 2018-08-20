"""Check whether a package name is available on PyPi"""

import argparse
import requests

BASE_URL = 'https://pypi.org/pypi'


def get_response(name):
    """Request response from PyPi API"""
    target_url = '{0}/{1}/json'.format(BASE_URL, name)
    r = requests.get(target_url)

    if r.status_code == 404:
        response = None
    else:
        response = r.json()

    return response


def is_name_taken(name):
    """Check module filename for conflict"""
    response = get_response(name)

    if response:
        file_name = response.get('urls')[0].get('filename').split('-')[0]
        return True if name.lower() == file_name.lower() else False

    return False


def main():
    """Handle arguments and flow"""
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='name of the package you want to check', type=str)
    args = parser.parse_args()

    if is_name_taken(args.name):
        print('`{0}` is unavailable.'.format(args.name))
    else:
        print('`{0}` is available'.format(args.name))


if __name__ == '__main__':
    main()
