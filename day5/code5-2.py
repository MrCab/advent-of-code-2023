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
    self.thingsMapped = {}

class SeedMapper :
  def __init__( self, ds=0, ss=0, r=0 ):
    self.sourceStart = ss
    self.destStart = ds
    self.range = r


# 90% using this class as a namespace
class SeedSolver :

  #DEFAULT_FILE = "day5\\input5-sample.txt"
  DEFAULT_FILE = "day5\\input5.txt"
  DAY = 5
  verbosePrint = True

  allTheSeeds = []
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
    self.allTheSeeds = []

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

  def slowProcessInput( self ) :
    # The first line is seed IDs
    seedRanges = re.split( "\D+", self.seedInfo[0] )[1:]

    i = 0
    while i < len( seedRanges ) :
      self.seeds = self.parseSeedRanges( seedRanges[i:i+1] )
      self.processInput()
      self.processSeedLocations()
      print( self.getLowestField() )
      i+= 2

  #####

  def parseSeedRanges( self, seedInput ) :
    if len( seedInput ) % 2 != 0 :
      print( "WHY HAVE FARMS FORSAKEN US" )
      exit( 1 )
    seedList = []

    i = 0
    while i < len( seedInput ) :
      seed = int( seedInput[ i ] )
      range = int( seedInput[ i + 1 ] )
      j = 0
      while j < range :
        seedList.append( seed + j )
        j += 1
      i += 2

    return seedList
    
  #####

  def readInput( self, fileName ) :
    foo = open( fileName, 'r').readlines()

    #trim the lines
    self.seedInfo = [ x.rstrip("\n") for x in foo ]

  #####

  def processInput( self ) :

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
#      DebugPrinter.debugPrint( line )
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
    for seed in self.seeds :
      DebugPrinter.debugPrint( seed )

      key = "seed"
      thisSeed = SeedMap()
      thisSeed.thingsMapped[ key ] = int(seed)
      while ( key in self.mappers ) :
        #Assumption - in part 1, there's only one mapping TEXT
        # (so if there's seeds to soil, there is no seeds to light)
        nextKey = list( self.mappers[ key ].keys() )[0]

        #default to same value
        thisSeed.thingsMapped[ nextKey ] = thisSeed.thingsMapped[ key ]

        for range in self.mappers[ key ][ nextKey ] :
          if thisSeed.thingsMapped[ key ] >= range.sourceStart and thisSeed.thingsMapped[ key ] < ( range.sourceStart + range.range ) :
            thisSeed.thingsMapped[ nextKey ] = range.destStart + ( thisSeed.thingsMapped[ key ] - range.sourceStart )
            DebugPrinter.debugPrint( str( range.sourceStart ) + " :: " + str( range.destStart ) + " :: " + str( range.range ) )
            DebugPrinter.debugPrint( str( range.destStart ) + " + " + str( thisSeed.thingsMapped[ key ] ) + " - " + str( range.sourceStart ) + " = " + str( thisSeed.thingsMapped[ key ] - range.sourceStart ) ) 
            DebugPrinter.debugPrint( key + " -> " + nextKey + " = " + str( thisSeed.thingsMapped[ nextKey ] ) )
            break
        key = nextKey
        #DebugPrinter.debugPrint( key + " = " + str( thisSeed.thingsMapped[ key ] ) )
      DebugPrinter.debugPrint( "-------------" )
      self.allTheSeeds.append( thisSeed )

  #####

  def getLowestField( self ) :
    lowest = self.allTheSeeds[0].thingsMapped[ "location" ]
    for seed in self.allTheSeeds :
      #DebugPrinter.debugPrint( str( seed.thingsMapped["location"] ) )
      lowest = min( lowest, seed.thingsMapped["location"])
    return lowest

  #####

  def main(self) :

    self.processArguments()

    # so plugging in all the numbers at once breaks things...so do it a little at a time
    self.slowProcessInput()
    #self.processInput()
    #self.processSeedLocations()
    #print( self.getLowestField() )


if __name__ == "__main__":
  p = SeedSolver() 
  p.main()
