import re

foo = open('input1-1.txt', 'r').readlines()

sumtotal = 0

for bar in foo :
  first = re.sub( "^\D*(\d).*\n", "\g<1>", bar)
  last = re.sub( "^.*(\d)\D*\n", "\g<1>", bar)
  number = int( first + last )
  sumtotal += number

print ( sumtotal )

