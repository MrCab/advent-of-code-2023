import re

foo = open('input2-1.txt', 'r').readlines()

sumtotal = 0

cubes = {
  "red" : 12,
  "green" : 13,
  "blue" : 14
}

regexes = {}
for k in cubes.keys() :
  reg = re.compile( ".*?(\d+) " + k + ".*" )
  regexes[ k ] = reg

#print( regexes )

###########
def checkGame( gameBar, gameCubes, gameRegexes ) :
  isPossible = True
  games = gameBar.split( ";" )

  for game in games :
#    print( "Game --" + game )
    for color in gameCubes.keys() :
#      print( "---checking " + color )
      m = gameRegexes[ color ].match( game )
#      print ( m )
      if m :
#        print( m.group(1) + " >>> " + str( gameCubes[ color ] ) )
        if int( m.group(1) ) > gameCubes[ color ] :
          isPossible = False
#          print ("Impossible Game - " + gameBar )
          return False
  return isPossible
###########

for bar in foo :

  GameID = re.sub( "Game (\d+):.*\n", "\g<1>", bar )
  if checkGame( bar, cubes, regexes ) :
    sumtotal += int( GameID )

print ( sumtotal )

