import re
import argparse

class DebugPrinter :

  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )


class SpiritTempleSolver :

  DEFAULT_FILE = "day8\\input8.txt"
  DAY = 8
  verbosePrint = True

  #directions = []
  #nodes = {}
  #steps = 0

  ####
  # Leaving the constructor here so I remember how to do it.
  # should proabbly put the "constant" regex compiling here

  def __init__( self ):
    self.steps = 0
    self.nodes = {}
    self.directions = []
    self.start = "AAA"
    self.destination = "ZZZ"

  #####

  def processArguments( self ) :
    # parse the input, if any
    parser = argparse.ArgumentParser(description=f'AOC2023 Puzzle Day { self.DAY }')
    parser.add_argument("-i", "--input", help="Input File if not default", action='store', default=self.DEFAULT_FILE )
    parser.add_argument("-v", "--verbose", help="Print verbose test output", action='store_true', default=SpiritTempleSolver.verbosePrint )
    args = parser.parse_args()

    DebugPrinter.verbose = args.verbose

    # process the input file
    self.readInput( args.input )

  #####

  def readInput( self, fileName ) :
    foo = open( fileName, 'r').readlines()

    #trim the lines
    foo = [ x.rstrip("\n") for x in foo ]

    # The first line is directions
    self.directions = [*foo.pop(0) ]

    # the second line is blank
    foo.pop(0)

    # I made this up but who knows what part 2 is
    #### SPECIAL - the first node is the starting point
    ####self.start = re.split( "[^A-Z]+", foo[0] )[0]

    for line in foo :
      n = re.split( "[^A-Z]+", line )
      self.nodes[ n[0] ] = { "L" : n[1], "R" : n[2] }

  #####

  def findSpiritTemple( self ) :
    step = 0
    curNode = self.start
    i = 0

    while curNode != self.destination :
      curNode = self.nodes[ curNode ][ self.directions[ i ] ]
      step += 1
      i += 1
      if i == len(self.directions) : i = 0
    self.steps = step
    print( step )

  #####

  def main(self) :

    self.processArguments()
    self.findSpiritTemple()

if __name__ == "__main__":
  p = SpiritTempleSolver() 
  p.main()
