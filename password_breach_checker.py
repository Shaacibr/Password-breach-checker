import requests
import hashlib
import sys




def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    resp = requests.get(url)
    if resp.status_code != 200:
        raise RuntimeError(f'Error Fetching: {resp.status_code}, check the API and Try Again')
    return resp


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


#check password if exists in API response
def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    # print(first5_char, tail)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times..... you should change!')
        else:
            print(f'{password} was not found. Carry ON!')
    return 'Done!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

