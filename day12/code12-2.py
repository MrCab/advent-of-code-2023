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

class LineOfSprings :

  workingSpring = "."
  newWorkingSpring = "W"
  borkedSpring = "#"
  oldMaybe = "?"
  newMaybe = "M"

  doomTuple = [ newWorkingSpring, borkedSpring ]


  def __init__ ( self, line, nums ) :
    self.linup = line.replace( self.workingSpring, self.newWorkingSpring ).replace( self.oldMaybe, self.newMaybe )
    self.picross = nums
    self.theGodPattern = ""

  def countPossibilities( self ) :

    thePattern = "^"
    for i in self.picross :
      thePattern += "%s+%s{%d}" % ( self.newWorkingSpring, self.borkedSpring, i )
    thePattern += self.newWorkingSpring + "+$"
    self.theGodPattern = re.compile( thePattern )

    return self.findThings( self.newWorkingSpring + self.linup + self.newWorkingSpring )

######

  def findThings( self, line ) :
    matches = 0

    if line.find( self.newMaybe ) == -1 :
      return 0

#// ?#?#??#?#.#?? 1,1,4,1
#// ??#???????#?????? 7,1,1,1
    for t in self.doomTuple :
      mySub = line.replace( self.newMaybe, t, 1 )
      if self.theGodPattern.match( mySub ) :
        matches += 1
      matches += self.findThings( mySub )
    return matches
      
class SpringSolver :

  DEFAULT_FILE = "day12\\input12.txt"
  DAY = 12
  verbosePrint = True

  ####
  # Leaving the constructor here so I remember how to do it.
  # should proabbly put the "constant" regex compiling here

  def __init__( self ):
    self.sumTotal = 0
    self.springLines = []

  #####

  def processArguments( self ) :
    # parse the input, if any
    parser = argparse.ArgumentParser(description=f'AOC2023 Puzzle Day { self.DAY }')
    parser.add_argument("-i", "--input", help="Input File if not default", action='store', default=self.DEFAULT_FILE )
    parser.add_argument("-v", "--verbose", help="Print verbose test output", action='store_true', default=SpringSolver.verbosePrint )
    args = parser.parse_args()

    DebugPrinter.verbose = args.verbose

    # process the input file
    self.readInput( args.input )

  #####

  def readInput( self, fileName ) :
    foo = open( fileName, 'r').readlines()

    #trim the lines
    self.allLines = [ x.rstrip("\n") for x in foo ]

    for line in self.allLines :
      x = line.split(" ")

      # part 2
      springLine = x[0] + "?" + x[0] + "?" + x[0] + "?" + x[0] + "?" + x[0]
      picrossLine = [ int(x) for x in x[1].split(",") ] * 5


      self.springLines.append( LineOfSprings( springLine, picrossLine ) )

  #####

  def processAllSprings( self ) :
    unlimitedPossibilities = 0

    for line in self.springLines :
      unlimitedPossibilities += line.countPossibilities()

    print ( unlimitedPossibilities )

  #####

  def main(self) :

    self.processArguments()
    self.processAllSprings()
    

if __name__ == "__main__":
  p = SpringSolver() 
  p.main()
