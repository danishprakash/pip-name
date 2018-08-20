"""Check whether a package name is available on PyPi"""

import argparse
import requests

BASE_URL = 'https://pypi.org/pypi'
RED      = '\033[31m'
BOLD     = '\033[1m'
GREEN    = '\033[32m'
RESET    = '\033[0m'


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
        print('{0}{1}{2} is unavailable.'.format(RED, args.name, RESET))
    else:
        print('{0}{1}{2} is available'.format(GREEN, args.name, RESET))


if __name__ == '__main__':
    main()
