import re
import argparse
import math

class DebugPrinter :
  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )


#########

class StarSolver :

  DEFAULT_FILE = "day11\\input11.txt"
  DAY = 11
  verbosePrint = True

  ####
  # Leaving the constructor here so I remember how to do it.
  # should proabbly put the "constant" regex compiling here

  def __init__( self ):
    self.sumTotal = 0
    self.allLines = []
    self.nodes = []
    self.oneBlanks = []
    self.twoBlanks = []
    self.multiplier = 1000000

  #####

  def processArguments( self ) :
    # parse the input, if any
    parser = argparse.ArgumentParser(description=f'AOC2023 Puzzle Day { self.DAY }')
    parser.add_argument("-i", "--input", help="Input File if not default", action='store', default=self.DEFAULT_FILE )
    parser.add_argument("-v", "--verbose", help="Print verbose test output", action='store_true', default=StarSolver.verbosePrint )
    args = parser.parse_args()

    DebugPrinter.verbose = args.verbose

    # process the input file
    self.readInput( args.input )

  #####

  def readInput( self, fileName ) :
    foo = open( fileName, 'r').readlines()

    #trim the lines
    self.allLines = [ x.rstrip("\n") for x in foo ]

    galaxyChar = "#"

    # add left-to-right double space
    i = 0
    while i < len( self.allLines[0] ) :
      col = [ x[i] for x in self.allLines ]
      if col.count( galaxyChar ) == 0 :
        self.twoBlanks.append(i)
      i += 1

    # don't add the space in part 1 - we only need the coordinates
    i = 0
    while i < len( self.allLines ) :
      stars = self.allLines[ i ]
      index = stars.find( galaxyChar, 0 )
      if index == -1 :
        self.oneBlanks.append(i)
      else :
        while index >= 0 :
          self.nodes.append( ( i, index ) )
          index = stars.find( galaxyChar, index+1 )
      i += 1

  #####

  def processAllGalaxies( self ) :
    totalDistance = 0

    i = 0
    while i < len( self.nodes ) :
      j = i + 1
      while j < len( self.nodes ) :
        # all distances can only be in cardinal directions,
        # so just math the up=down and left-rigth distance
        y = abs( self.nodes[i][0] - self.nodes[j][0])
        x = abs( self.nodes[i][1] - self.nodes[j][1])

        # add blanks
        xPath =  [ p+min(self.nodes[i][1], self.nodes[j][1]) for p in list( range( abs(self.nodes[i][1] - self.nodes[j][1]) ) ) ]
        xBoost = len( [p for p in xPath if p in self.twoBlanks ] )

        yPath =  [ p+min(self.nodes[i][0], self.nodes[j][0]) for p in list( range( abs(self.nodes[i][0] - self.nodes[j][0]) ) ) ]
        yBoost = len( [p for p in yPath if p in self.oneBlanks ] )


        totalDistance += x + y + ( ( self.multiplier - 1 ) * ( xBoost + yBoost ) )
        j += 1
      i += 1

    print ( totalDistance )

  #####

  def main(self) :

    self.processArguments()
    self.processAllGalaxies()
    

if __name__ == "__main__":
  p = StarSolver() 
  p.main()
