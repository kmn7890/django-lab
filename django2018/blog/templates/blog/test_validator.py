import re

val = "01012341234abc" #11자리
# val = "0101234123" 10자리

pattern = r"^01[016789][1-9]\d{6,7}$"



"""
010
011

"""


if re.match(pattern, val):
    print('matched')
else:
    print('invalid')