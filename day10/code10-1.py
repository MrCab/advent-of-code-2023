import re
import argparse

class DebugPrinter :
  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )


class World7Solver :

  DEFAULT_FILE = "day10\\input10.txt"
  DAY = 10
  verbosePrint = True

  KEYS = "F7LJ-|"

  ####
  # Leaving the constructor here so I remember how to do it.
  # should proabbly put the "constant" regex compiling here

  def __init__( self ):
    self.allLines = []
    self.distancesFromStart = []
    self.startNode = ( -1, -1 )
    self.maxDistance = 0
    self.nodesToCheck = []

  #####

  def processArguments( self ) :
    # parse the input, if any
    parser = argparse.ArgumentParser(description=f'AOC2023 Puzzle Day { self.DAY }')
    parser.add_argument("-i", "--input", help="Input File if not default", action='store', default=self.DEFAULT_FILE )
    parser.add_argument("-v", "--verbose", help="Print verbose test output", action='store_true', default=World7Solver.verbosePrint )
    args = parser.parse_args()

    DebugPrinter.verbose = args.verbose

    # process the input file
    self.readInput( args.input )

  #####

  def readInput( self, fileName ) :
    foo = open( fileName, 'r').readlines()
    self.distancesFromStart = [None] * len( foo )

    self.allLines = []
    i = 0
    #trim the lines
    while i < len( foo ):
#    self.allLines = [ x.rstrip("\n") for x in foo ]
      x = foo[i]
      self.allLines.append( x.rstrip( "\n" ) )
      self.distancesFromStart[i] = [None] * len(x)

      theS = x.find("S")
      if theS > -1 :
        self.startNode = ( theS, i )
        self.distancesFromStart[i][theS] = 0
      i += 1

  #####

  def getNeighbors( x, y, node ) :
    neighbors = []

    if node == "F" :
      neighbors = [( x+1, y ), (x, y+1) ]
    elif node == "7" :
      neighbors = [ (x-1, y),(x, y+1)]
    elif node == "J" :
      neighbors = [ (x, y-1), (x-1, y ) ]
    elif node == "L" :
      neighbors = [ ( x+1, y), (x, y-1)]
    elif node == "-" :
      neighbors = [ ( x-1, y), (x+1, y)]
    elif node == "|" :
      neighbors = [ ( x, y-1), (x, y+1)]
    return neighbors

  #####

  def markNode( self, x, y, oldValue ) :
    if self.distancesFromStart[ y ][ x ] is None :
      self.distancesFromStart[ y ][ x ] = oldValue + 1
      self.nodesToCheck.append( ( x, y ) )

  #####

  def addNextPipe( self, x, y ) :
    node = self.allLines[ y ][ x ]
    myDistance = self.distancesFromStart[ y ][ x ]
    self.maxDistance = max( myDistance, self.maxDistance )

    DebugPrinter.debugPrint( "%s @ (%d,%d)" % (node, x, y ) )


    neighbors = World7Solver.getNeighbors( x, y, node )

    # distances = []
    # distances.append( self.distancesFromStart[ neighbors[0][ 1 ] ][ neighbors[0 ][0]] )
    # distances.append( self.distancesFromStart[ neighbors[ 1 ][ 1 ] ][ neighbors[ 1 ][0]] )

    # if the neighbors have the same value, or if one of them is ths same as this node, then this is the distance and we're done
#    if distances[0] == distances[1] or\
#       distances[0] == myDistance or\
#       distances[1] == myDistance :
#      return myDistance
#    else :
    self.markNode( neighbors[0][0], neighbors[0][1], myDistance )
    self.markNode( neighbors[1][0], neighbors[1][1], myDistance )

  #####

  def world7RandoRouter( self ) :

    ###########
    # special check for start node neighbors
    y = self.startNode[1] - 1
    x = self.startNode[0]
    if y > -1 and self.allLines[y][ x ] in "|F7" :
      self.markNode( x, y, 0 )

    y = self.startNode[1] + 1
    if y < len( self.allLines ) and self.allLines[y][ x ] in "|JL" :
      self.markNode( x, y, 0 )

    y = self.startNode[1]
    x = self.startNode[0] - 1
    if x > -1 and self.allLines[y][ x ] in "-LF" :
      self.markNode( x, y, 0 )

    x = self.startNode[0] + 1
    if x < len( self.allLines[y] ) and self.allLines[y][ x ] in "|J7" :
      self.markNode( x, y, 0 )

    DebugPrinter.debugPrint( self.nodesToCheck )
    #########

    while len( self.nodesToCheck ) > 0 :
      a = self.nodesToCheck.pop(0)
      self.addNextPipe( a[0],a[1] )

    print( self.maxDistance )

  #####

  def main(self) :

    self.processArguments()
    self.world7RandoRouter()
    

if __name__ == "__main__":
  p = World7Solver() 
  p.main()
