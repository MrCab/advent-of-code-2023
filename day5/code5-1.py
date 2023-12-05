import re
import argparse

class DebugPrinter :

  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )


class SeedMap :

  def __init__( self ):
    self.seed = 0
    self.soil = 0
    self.fertalizer = 0
    self.water = 0
    self.light = 0
    self.humidity = 0
    self.location = 0
    self.thingsMapped = {}

class SeedMapper :
  def __init__( self, ss=0, ds=0, r=0 ):
    self.sourceStart = ss
    self.destStart = ds
    self.range = r


# 90% using this class as a namespace
class SeedSolver :

  DEFAULT_FILE = "day5\\input5.txt"
  DAY = 5
  verbosePrint = True

  fields = []
  mappers = {}

  mapTextRegex = re.compile( "([a-zA-Z]+)-to-([a-zA-Z]+) map:" )
  # skipping in favor of just splitting the line
  #mapNumbersRegex = re.compile( "(\d+) (\d+) (\d+)")

  ####
  # Leaving the constructor here so I remember how to do it.
  # should proabbly put the "constant" regex compiling here

  def __init__( self ):
    self.lowest = -1
    self.mappers = {}
    self.fields = []

  #####

  def processArguments( self ) :
    # parse the input, if any
    parser = argparse.ArgumentParser(description=f'AOC2023 Puzzle Day { self.DAY }')
    parser.add_argument("-i", "--input", help="Input File if not default", action='store', default=self.DEFAULT_FILE )
    parser.add_argument("-v", "--verbose", help="Print verbose test output", action='store_true', default=SeedSolver.verbosePrint )
    args = parser.parse_args()

    DebugPrinter.verbose = args.verbose

    # process the input file
    self.readInput( args.input )

  #####

  def readInput( self, fileName ) :
    foo = open( fileName, 'r').readlines()

    #trim the lines
    self.seedInfo = [ x.rstrip("\n") for x in foo ]

  #####

  def processInput( self ) :

    # The first line is seed IDs
    self.seeds = re.split( "\D", self.seedInfo[0] )[1:]

    # start reading from line 3
    i = 2
    mapSource = ""
    mapDest = ""

    while i < len( self.seedInfo ) :
      line = self.seedInfo[i]
      textMatch = self.mapTextRegex.match( line )
      
      # after seeds, there are 3 types of lines
      # x-to-y
      # (blank lines)
      # three numbers describing a mapping
      DebugPrinter.debugPrint( line )
      if textMatch :
        mapSource = textMatch.group(1)
        mapDest = textMatch.group(2)

        if not mapSource in self.mappers :
          self.mappers[ mapSource ] = {}
        self.mappers[ mapSource ][ mapDest ] = []
      elif line != "" :
        ranges = re.split( "\D+", line )
        s = SeedMapper( int(ranges[0]), int(ranges[1]), int(ranges[2] ) )
        self.mappers[ mapSource ][ mapDest ].append( s )

      i += 1

  #####

  def processSeedLocations( self ) :
    print ( "hello world" )

  #####

  def main(self) :

    self.processArguments()
    self.processInput()
    self.processSeedLocations()


if __name__ == "__main__":
  p = SeedSolver() 
  p.main()
