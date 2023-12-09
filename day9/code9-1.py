import re
import argparse

class DebugPrinter :
  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )

class ONodes :

  def __init__( self, val, lp="", rp="" ) :
    self.value = val
    self.leftChild = None
    self.rightChild = None
    self.leftParent = lp
    self.rightParent = rp

#########

class OasisSolver :

  DEFAULT_FILE = "day9\\input9.txt"
  DAY = 9
  verbosePrint = True

  ####
  # Leaving the constructor here so I remember how to do it.
  # should proabbly put the "constant" regex compiling here

  def __init__( self ):
    self.sumTotal = 0
    self.allLines = []

  #####

  def processArguments( self ) :
    # parse the input, if any
    parser = argparse.ArgumentParser(description=f'AOC2023 Puzzle Day { self.DAY }')
    parser.add_argument("-i", "--input", help="Input File if not default", action='store', default=self.DEFAULT_FILE )
    parser.add_argument("-v", "--verbose", help="Print verbose test output", action='store_true', default=OasisSolver.verbosePrint )
    args = parser.parse_args()

    DebugPrinter.verbose = args.verbose

    # process the input file
    self.readInput( args.input )

  #####

  def readInput( self, fileName ) :
    foo = open( fileName, 'r').readlines()

    #trim the lines
    self.allLines = [ x.rstrip("\n") for x in foo ]

  #####

  def processAllLines( self ) :
    sumTotal = 0
    for line in self.allLines :
      # Initialize a line of nodes
      nums = [ int(x) for x in line.split() ]

      nodes = [ ONodes( x, None, None ) for x in nums ]

      sumTotal += nums[-1] + self.mathALine( nodes )
    print( sumTotal )

  #####

  def mathALine( self, oNodes ) :
    
    i = 0
    childONodes = []
    vals = set()
    valA = []
    returnMe = 0

    while i < ( len( oNodes ) - 1 ) :
      newVal = oNodes[ i + 1 ].value - oNodes[i].value
      vals.add( newVal )
      valA.append( newVal )
      childONodes.append( ONodes( newVal, oNodes[i], oNodes[i+1] ) )
      i += 1
    
    # if all the values match, return that value
    if len( vals ) == 1 :
      returnMe = list(vals)[0]
    # Else, recurse, and add the value to the last node
    else:
      returnMe = childONodes[-1].value + self.mathALine( childONodes )
    return returnMe

  #####

  def main(self) :

    self.processArguments()
    self.processAllLines()
    

if __name__ == "__main__":
  p = OasisSolver() 
  p.main()
