import re
import argparse
#import math

class DebugPrinter :
  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )

######

class BunnySolver :

  DEFAULT_FILE = "day16\\input16.txt"
  DAY = 16
  verbosePrint = True

  # Setup for next path
  nextSpot = {}

  nextSpot['R'] = {}
  nextSpot['R']['.'] = "R"
  nextSpot['R']['/'] = "U"
  nextSpot['R']['\\'] = "D"
  nextSpot['R']['|'] = "UD"
  nextSpot['R']['-'] = "R"

  nextSpot['L'] = {}
  nextSpot['L']['.'] = "L"
  nextSpot['L']['/'] = "D"
  nextSpot['L']['\\'] = "U"
  nextSpot['L']['|'] = "UD"
  nextSpot['L']['-'] = "L"

  nextSpot['U'] = {}
  nextSpot['U']['.'] = "U"
  nextSpot['U']['/'] = "R"
  nextSpot['U']['\\'] = "L"
  nextSpot['U']['|'] = "U"
  nextSpot['U']['-'] = "LR"

  nextSpot['D'] = {}
  nextSpot['D']['.'] = "D"
  nextSpot['D']['/'] = "L"
  nextSpot['D']['\\'] = "R"
  nextSpot['D']['|'] = "D"
  nextSpot['D']['-'] = "LR"

  ####
  # Leaving the constructor here so I remember how to do it.
  # should proabbly put the "constant" regex compiling here

  def __init__( self ):
    self.sumTotal = 0
    self.allLines = []
    self.energizer = []
    self.discordWillHateMe = []

  #####

  def processArguments( self ) :
    # parse the input, if any
    parser = argparse.ArgumentParser(description=f'AOC2023 Puzzle Day { self.DAY }')
    parser.add_argument("-i", "--input", help="Input File if not default", action='store', default=self.DEFAULT_FILE )
    parser.add_argument("-v", "--verbose", help="Print verbose test output", action='store_true', default=BunnySolver.verbosePrint )
    args = parser.parse_args()

    DebugPrinter.verbose = args.verbose

    # process the input file
    self.readInput( args.input )

  #####

  def readInput( self, fileName ) :
    foo = open( fileName, 'r').readlines()

    #trim the lines
    for line in foo :
      self.allLines.append( *[line.rstrip("\n") ] )
      self.energizer.append( [""] * len(line) )

  #####

  def goToTheLight( self, startX, startY, going ) :
    if self.energizer[startY][startX].find( going ) == -1 :
      self.energizer[startY][startX] += going
    else :
      return
    # loop detection
#    if self.energizer[startY][startX] > 100 :
#      return

    space = self.allLines[startY][startX]
    nextSpace = BunnySolver.nextSpot[going][space]

    for n in nextSpace :
      appendMe = None
      if n == 'D' and startY +1 < len(self.allLines):
        appendMe = ( "self.goToTheLight(%d,%d,'%s')" % (startX, startY+1, n) )
      elif n == 'U' and startY > 0 :
        appendMe = ( "self.goToTheLight(%d,%d,'%s')" % (startX, startY-1, n) )
      elif n == "L" and startX > 0 :
        appendMe = ( "self.goToTheLight(%d,%d,'%s')" % (startX-1, startY, n) )
      elif n == "R" and startX+1 < len(self.allLines[startY]) :
        appendMe = ( "self.goToTheLight(%d,%d,'%s')" % (startX+1, startY, n) )
      
      if appendMe :
        self.discordWillHateMe.append( appendMe )

  def countOfEnergized(self) :
    count = 0
    for line in self.energizer :
      count += len(line) - line.count("")
    return count

  #####

  def main(self) :

    self.processArguments()
    self.discordWillHateMe.append( "self.goToTheLight(0,0, 'R')" )
    while len( self.discordWillHateMe ) > 0 :
      foo = self.discordWillHateMe.pop(0)
      exec( foo )
    print( self.countOfEnergized() )

    

if __name__ == "__main__":
  p = BunnySolver() 
  p.main()
