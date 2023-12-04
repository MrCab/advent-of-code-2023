import re

foo = open('input4.txt', 'r').readlines()

#trim the lines
foo = [ re.sub("\n", "", x ) for x in foo ]

sumtotal = 0

cardLineRegex = re.compile( '^Card\s+(\d+):([ 0-9]+)\|(.*)$' )


for bar in foo :

  winCount = 0

  lineMatch = cardLineRegex.match( bar )
  if lineMatch :

#    print( lineMatch )

    winners = re.split( '\s+', lineMatch.group(2) )
    myNums = " " + lineMatch.group(3) + " "
    print( "++++WINNERS - " + str( winners ) )
    print( "$$$$MY NUMS = |" + myNums + "|" )

    for num in winners :
      if len( num ) == 0 : continue

#      print( num + " - " + str( re.search( '\s' + num + '\s' , myNums ) ) )
#      print( num + " - " + str( len( re.split( '\s' + num + '\s' , myNums ) ) - 1 ) )
      a = len( re.split( '\s' + num + '\s' , myNums ) ) - 1
      if a > 1 : print( "OMG" )
      
      if re.search( '\s' + num + '\s' , myNums ) :
        if winCount >= 1 :
          winCount *= 2
        else :
          winCount = 1
        print( "-----Found " + num + " - new winCount = " + str( winCount ) )
    print( "Card " + lineMatch.group( 1 ) + " adding wincount - " + str( winCount ) )
  sumtotal += winCount
#  print( "Running Total = " + str( sumtotal ) )

print ( sumtotal )

