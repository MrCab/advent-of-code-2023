import re

foo = open('input4.txt', 'r').readlines()

#trim the lines
foo = [ re.sub("\n", "", x ) for x in foo ]

sumtotal = 0

cardLineRegex = re.compile( '^Card\s+(\d+):([ 0-9]+)\|(.*)$' )

cardCopies = {}

i = 0
while i < len( foo ) :
  i += 1
  cardCopies[ str(i) ] = 1

for bar in foo :

  cardNum = 0
  lineMatch = cardLineRegex.match( bar )
  if lineMatch :

#    print( lineMatch )

    cardNum = int( lineMatch.group(1) )
    winners = re.split( '\s+', lineMatch.group(2) )
    myNums = " " + lineMatch.group(3) + " "

    MATCHCOUNT = len( [ x for x in winners if re.search( '\s' + x + '\s' , myNums ) ]  ) - 2
    print( "=====MATCHCOUNT = " + str( MATCHCOUNT ) )

    i = 0
    while i < MATCHCOUNT and i < ( len( foo ) + 1 ):
      i += 1
      index = str( cardNum )
      print( "-- adding " + str( cardCopies[ str( cardNum ) ] ) + " to " + index )
      cardCopies[ str( i + cardNum ) ] += cardCopies[ str( cardNum ) ]
    print( "Adding for " + str( cardNum) + " == " + str( cardCopies[ str( cardNum ) ] ) )
    sumtotal += cardCopies[ str( cardNum ) ] 

    print( sumtotal )
print( "cOPIES - " + str( sum( [ cardCopies[x] for x in cardCopies.keys() ] ) ) )

