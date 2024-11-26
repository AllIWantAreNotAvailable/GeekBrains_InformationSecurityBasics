import hashlib
import re
import sys

PATTERN = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'


def validate_by_regex(password:str, pattern:str=PATTERN) -> bool:
    return bool(re.match(pattern, ''.join([*filter(lambda _: not bool(re.match(r'[@$!%*#?&]', _)), password)])))


if __name__ == '__main__':
    usrPassword = sys.argv[1] if 1 < len(sys.argv) else input('Enter password to validate:\n>>> ')
    if validate_by_regex(usrPassword):
        print('sha256:', hashlib.sha256(usrPassword.encode()).hexdigest())
    else:
        print('Non valid')
