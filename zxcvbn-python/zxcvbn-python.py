#this is a program

from zxcvbn import zxcvbn

results = zxcvbn('this is a good password', user_inputs=['Chris', 'Ross', 'Christopher'])

print(results)
