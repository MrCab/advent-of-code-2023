import re

foo = open('input2-1.txt', 'r').readlines()

sumtotal = 0

colors = ["red", "blue", "green" ]

regexes = {}
for k in colors :
  reg = re.compile( ".*?(\d+) " + k + ".*" )
  regexes[ k ] = reg

#print( regexes )

###########
def gamePower( gameBar, gameRegexes ) :
  games = gameBar.split( ";" )

  colors = {}
  for c in gameRegexes.keys() :
    colors[ c ] = 1 # are zero cubes possible?

  for game in games :
#    print( "Game --" + game )
    for color in gameRegexes.keys() :
#      print( "---checking " + color )
      m = gameRegexes[ color ].match( game )
#      print ( m )
      if m :
#        print( m.group(1) + " >>> " + str( colors[ color ] ) )
        if int( m.group(1) ) > colors[ color ] :
          colors[ color ] = int( m.group(1) )

  myPow = 1
  for c in colors.keys() :
    myPow *= colors[c]

  return myPow
###########

for bar in foo :

  GameID = re.sub( "Game (\d+):.*\n", "\g<1>", bar )
  pow = gamePower( bar, regexes ) 
  sumtotal += pow
#  break

print ( sumtotal )

