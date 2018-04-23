# Functions Common with Game of Life

from Matrix import *
from VarDefines import *

class ApplyRules:

    def __init__( self, BitMatrix ):

        self.SizeLines = 0
        self.SizeCollumns = 0

        self.Matrix = BitMatrix

        self.CountAliveCells = 0

    def ApplyRulesFunction( self ):

        self.SizeLines = len(self.Matrix) - 2
        self.SizeCollumns = len(self.Matrix[0]) - 2

        self.NewGeneration( )

        return self.Matrix

    def NewGeneration( self ):

        for line in range( 1, self.SizeLines ):
            for collumn in range( 1, self.SizeCollumns ):

                self.CountAliveCells = 0
                self.CheckNeighbors( line, collumn )

        self.RefactorMatrix()

    def CheckNeighbors( self, line, collumn ):

        for lineTemp in range( (line - 1), (line + 2) ):
            for collumnTemp in range( (collumn - 1), (collumn + 2) ):

                if( lineTemp != line or collumnTemp != collumn ):
                    if( self.Matrix[lineTemp][collumnTemp] == Live
                    or self.Matrix[lineTemp][collumnTemp] == AliveCellWillDie
                    or self.Matrix[lineTemp][collumnTemp]  == AliveCellWillLive ):
                        self.CountAliveCells += 1


        self.CheckAliveCellWithLessTwoAliveNeighbors( line, collumn )
        self.CheckAliveCellWithMoreThreeAliveNeighbors( line, collumn )
        self.CheckAliveCellWithTwoThreeAliveNeighbors( line, collumn )
        self.CheckDeadCellWithThreeAliveNeighbors( line, collumn )

    def RefactorMatrix( self ):

        for line in range( 1, self.SizeLines ):
            for collumn in range( 1, self.SizeCollumns ):

                if( self.Matrix[line][collumn] == DeathCellWillLive
                or self.Matrix[line][collumn] == AliveCellWillLive ):

                    self.Matrix[line][collumn] = Live

                if( self.Matrix[line][collumn] == AliveCellWillDie ):

                    self.Matrix[line][collumn] = Dead

    def CheckAliveCellWithLessTwoAliveNeighbors( self, line, collumn ):

        if( self.Matrix[line][collumn] == Live and self.CountAliveCells < 2 ):

            self.Matrix[line][collumn] = AliveCellWillDie

    def CheckAliveCellWithMoreThreeAliveNeighbors( self, line, collumn ):

        if( self.Matrix[line][collumn] == Live and self.CountAliveCells > 3 ):

            self.Matrix[line][collumn] = AliveCellWillDie

    def CheckAliveCellWithTwoThreeAliveNeighbors( self, line, collumn ):

        if( (self.Matrix[line][collumn] == Live and self.CountAliveCells == 2)
        or (self.Matrix[line][collumn] == Live and self.CountAliveCells == 3) ):

            self.Matrix[line][collumn] = AliveCellWillLive

    def CheckDeadCellWithThreeAliveNeighbors( self, line, collumn ):

        if( self.Matrix[line][collumn] == Dead and self.CountAliveCells == 3 ):

            self.Matrix[line][collumn] = DeathCellWillLive

class DrawMatrix:

    def __init__( self, BitMatrix, Canvas ):

        self.Matrix = BitMatrix
        self.Canvas = Canvas

    def DrawMatrixFunction( self ):

        leftTopBotPoints = 0
        rightTopBotPoints = 15

        topStaticPoint = 0
        botStaticPoint = 15

        for line in range( 1, LineTotalSize - 2 ):

            for collumn in range( 1, CollumnTotalSize - 2 ):

                self.Grid = [leftTopBotPoints,topStaticPoint,leftTopBotPoints,botStaticPoint,rightTopBotPoints,botStaticPoint,rightTopBotPoints,topStaticPoint]

                if( self.Matrix[line][collumn] == Live ):

                    Matrix = self.Canvas.create_polygon(self.Grid , fill='BLACK', outline='WHITE', tag='BlackBox')

                else:

                    Matrix = self.Canvas.create_polygon(self.Grid , fill='', outline='WHITE', tag='WhiteBox')

                leftTopBotPoints += 15
                rightTopBotPoints += 15

            topStaticPoint += 15
            botStaticPoint += 15

            leftTopBotPoints = 0
            rightTopBotPoints = 15
