import re

debugging = True

# Read the input file
foo = open('input3-1.txt', 'r').readlines()


# add extra lines for padding
foo.insert( 0, "" )
foo.append( "" )

sumtotal = 0

# regex to look for the first number in a string.
# Capture groups
# 1) beginning of the string until group 2
# 2) character before group 3
# 3) the first number in the string 
# 4) the character after group 3
# 5) everything after group 4 in the string

baseRegex = "^(\D*)(\D)(\d+)(\D)(.*)$"
startingRegex = re.compile( baseRegex )

# Matches any string containing what the problem considers a symbol
symbolRegex = re.compile( "^.*[^a-zA-Z0-9.].*$" )


#########
def debugPrint( line ) :
  if debugging :
    print( line )
##########

#######
# returns true if both of these are true
# - line matches lineRegex
# - the match's first capture group matches symbolRegex
#######
def checkLine( line, lineRegex ) :
  m = lineRegex.match( line )
  if m :
    debugPrint( "+++++++ matched " + str(m) )
    return symbolRegex.match( m.group(1) )
#######


# Use i so we can easily access the surrounding lines
i = 0
while ( i < ( len(foo) - 1 ) ) :
 
  debugPrint( i )

  # change the next line to contain extra padding
  # make room on each side to now break the regex
  # also kill the trailing newline
  foo[ i + 1 ] = "." + foo[ i + 1 ][0:-1] + "."

  bar = foo[i] 

  # note i = 0 should ALWAYS fail this
  m = startingRegex.match( bar )

  debugPrint( bar )

  while m :

    debugPrint( "-- checking " + str(m) )

    addToNumber = False
    number = int( m.group( 3 ) )

    # check the surrounding characters
    if symbolRegex.match( m.group(2) ) or symbolRegex.match( m.group(4) ) :
       debugPrint( "---Surrounding Match" )
       addToNumber = True

    else:
       # build a regex to capture the above and below bordering characters,
       # including diagonals
       sizeOfCheck = str( int( len( m.group(3) ) + 2 ) )
       aboveBelowRegex = re.compile( "^.{" + str(len( m.group(1) )) + "}(.{" + sizeOfCheck + "})" )

       if checkLine( foo[ i - 1 ], aboveBelowRegex ) or\
          checkLine( foo[ i + 1 ], aboveBelowRegex ) :

             debugPrint( "----- above/below match" )
             addToNumber = True

    if addToNumber :
      debugPrint( "######## Adding " + str( number ) )
      sumtotal += number

    # replace the number we just checked with dots and try again    
    bar = m.group( 1 ) + m.group( 2 ) + re.sub( ".", ".", m.group( 3 ) ) + m.group( 4 ) + m.group(5)
    debugPrint( "new bar - " + bar )
    m = startingRegex.match( bar )

  # while loop
  i += 1

print ( sumtotal )

