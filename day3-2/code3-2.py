import re

debugging = True

# Read the input file
foo = open('input3-1.txt', 'r').readlines()


# add extra lines for padding
foo.insert( 0, "" )
foo.append( "" )

sumtotal = 0

# map gear coordinate tuples to numbers
gears = {}
gearChar = "*"

########
def addGearNumber( x, y, number ) :
  if not ( (x, y ) in gears.keys() ) :
    gears[ ( x, y ) ] = []
  gears[ ( x, y ) ].append( number )
########

def printGears( gearRequiredNumber ) :
  totalGearStr = 0

  for gear in gears.keys() :
    debugPrint( str( gear ) + " --> " + str( gears[ gear ] ) )
    if len( gears[ gear ] ) == 2 :
      totalGearStr += ( gears[ gear ][0] * gears[ gear ][ 1 ] )
  print ( "Gear Str = " + str( totalGearStr ) )

##################

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
def checkLine( line, lineRegex, xCor, row, number ) :
  m = lineRegex.match( line )
  if m :
    debugPrint( "+++++++ matched " + str(m) )

    if symbolRegex.match( m.group(1) ) :
      theMatch = m.group(1)
      i = 0
      while i < len( theMatch ) :
        if theMatch[ i ] == gearChar :
          addGearNumber( ( xCor + i + 1 ), row, number )
        i += 1 

      # if there was a symbol in the match...
      return True
  # in all other situations...
  return False
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

       # technically if we want the true gear coordinate, we need to remove 1 and 1 for the padding
       if m.group(2) == gearChar :
         xCor = len( m.group(1) ) + 1
         addGearNumber( xCor, i, number )
       if m.group(4) == gearChar :
         xCor = len( m.group(1) ) + 1 + len( m.group(3) ) + 1
         addGearNumber( xCor, i, number )


    else:
       # build a regex to capture the above and below bordering characters,
       # including diagonals
       sizeOfCheck = str( int( len( m.group(3) ) + 2 ) )
       xCor = len( m.group( 1 ) ) 
       aboveBelowRegex = re.compile( "^.{" + str( xCor ) + "}(.{" + sizeOfCheck + "})" )

       if checkLine( foo[ i - 1 ], aboveBelowRegex, xCor, i - 1, number ) or\
          checkLine( foo[ i + 1 ], aboveBelowRegex, xCor, i + 1, number ) :

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

print ( "Total Part 1 = " + str( sumtotal ) )
printGears( 2 )

