import re
import argparse


# 90% using this class as a namespace
class ScratcherSolver :

  DEFAULT_FILE = "input4.txt"
  DAY = 4

  verbosePrint = False

  scratchCards = []
  sumTotal = 0

  ####
  # Leaving the constructor here so I remember how to do it.
  # should proabbly put the "constant" regex compiling here

  def __init__( self ):
    self.sumTotal = 0

  #####

  def processArguments( self ) :
    # parse the input, if any
    parser = argparse.ArgumentParser(description=f'AOC2023 Puzzle Day { self.DAY }')
    parser.add_argument("-i", "--input", help="Input File if not default", action='store', default=self.DEFAULT_FILE )
    parser.add_argument("-v", "--verbose", help="Print verbose test output", action='store_true', default=False )
    args = parser.parse_args()

    self.verbosePrint = args.verbose

    # process the input file
    self.readInput( args.input )

  #####

  def debugPrint( self, message ) :
    if self.verbosePrint :
      print( message )

  #####

  def readInput( self, fileName ) :
    foo = open('input4.txt', 'r').readlines()

    #trim the lines
    self.scratchCards = [ x.rstrip("\n") for x in foo ]

  #####

  def main(self) :

    self.processArguments()

    # because I'm refactoring and this code already assumes these are local
    foo = self.scratchCards
    sumtotal = self.sumTotal

    cardLineRegex = re.compile( '^Card\s+(\d+):([ 0-9]+)\|(.*)$' )

    for bar in foo :

      winCount = 0

      lineMatch = cardLineRegex.match( bar )
      if lineMatch :

        self.debugPrint( lineMatch )

        winners = re.split( '\s+', lineMatch.group(2) )
        myNums = " " + lineMatch.group(3) + " "
        self.debugPrint( "++++WINNERS - " + str( winners ) )
        self.debugPrint( "$$$$MY NUMS = |" + myNums + "|" )


        # Because everyone in discord likes list comprehensions.
        # in caps because yes, I was in a mood at the time
        MATCHCOUNT = len( [ x for x in winners if re.search( '\s' + x + '\s' , myNums ) ]  ) - 2
        self.debugPrint( "=====MATCHCOUNT = " + str( MATCHCOUNT ) )


        for num in winners :
          if len( num ) == 0 : continue

          # the second line here is checking if there are duplicate winning numbers in my numbers
          # 'Card 55: 1 2 3 | 4 5 2 2 2 2 6'
          self.debugPrint( num + " - " + str( re.search( '\s' + num + '\s' , myNums ) ) )
          self.debugPrint( num + " - " + str( len( re.split( '\s' + num + '\s' , myNums ) ) - 1 ) )

          a = len( re.split( '\s' + num + '\s' , myNums ) ) - 1
          if a > 1 : debugPrint( "OMG" )
      
          if re.search( '\s' + num + '\s' , myNums ) :
            if winCount >= 1 :
              winCount *= 2
            else :
              winCount = 1
            self.debugPrint( "-----Found " + num + " - new winCount = " + str( winCount ) )
        self.debugPrint( "Card " + lineMatch.group( 1 ) + " adding wincount - " + str( winCount ) )
      sumtotal += winCount
      self.debugPrint( "Running Total = " + str( sumtotal ) )

    print ( sumtotal )

if __name__ == "__main__":
  p = ScratcherSolver() 
  p.main()
