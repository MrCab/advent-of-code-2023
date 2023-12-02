import re

foo = open('input1-1.txt', 'r').readlines()

sumtotal = 0

for bar in foo :
  foobar = bar

  # Find first numbers
  bar = re.sub( "one","one1",bar )
  bar = re.sub( "two","two2",bar )
  bar = re.sub( "three","three3",bar )
  bar = re.sub( "four","four4",bar )
  bar = re.sub( "five","five5",bar )
  bar = re.sub( "six","six6",bar )
  bar = re.sub( "seven","seven7",bar )
  bar = re.sub( "eight","eight8",bar )
  bar = re.sub( "nine","nine9",bar )
  first = re.sub( "^\D*(\d).*\n", "\g<1>", bar)


  bar = foobar
  bar = re.sub( "one","1one",bar )
  bar = re.sub( "two","2two",bar )
  bar = re.sub( "three","3three",bar )
  bar = re.sub( "four","4four",bar )
  bar = re.sub( "five","5five",bar )
  bar = re.sub( "six","6six",bar )
  bar = re.sub( "seven","7seven",bar )
  bar = re.sub( "eight","8eight",bar )
  bar = re.sub( "nine","9nine",bar )
  last = re.sub( "^.*(\d)\D*\n", "\g<1>", bar)

  number = int( first + last )
  sumtotal += number

print ( sumtotal )

