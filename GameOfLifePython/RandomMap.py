# Random Map Of Game of Life

from Tkinter import *
from random import *
from Matrix import *
from Common import *
from VarDefines import *

class RandomMap:

    def __init__( self, Map, PreviousCanvas ):

        Map.geometry( '1335x650' )

        self.RandMap = Map
        self.PCanvas = PreviousCanvas

        self.Frame = Frame( self.RandMap )
        self.Frame["bg"] = "GRAY"
        self.Frame["bd"] = 1
        self.Frame.pack( side = LEFT )

        self.CanvasRandMap = Canvas( self.Frame )
        self.CanvasRandMap["bg"] = "GRAY"
        self.CanvasRandMap["width"] = 1199
        self.CanvasRandMap["heigh"] = 644
        self.CanvasRandMap["highlightbackground"] = "WHITE"
        self.CanvasRandMap.pack( side = LEFT )
        self.CanvasRandMap.create_text(100,40, text='Press Start to Play', fill='BLACK')

        self.ButtonStart = Button( self.Frame )
        self.ButtonStart["bg"] = "WHITE"
        self.ButtonStart["highlightbackground"] = "BLACK"
        self.ButtonStart["bd"] = 0
        self.ButtonStart["width"] = 10
        self.ButtonStart["text"] = "Start"
        self.ButtonStart["command"] = self.RunGameOfLife
        self.ButtonStart.pack( padx = 15, pady = 20 )

        self.ButtonBack = Button( self.Frame )
        self.ButtonBack["bg"] = "WHITE"
        self.ButtonBack["highlightbackground"] = "BLACK"
        self.ButtonBack["bd"] = 0
        self.ButtonBack["width"] = 10
        self.ButtonBack["text"] = "Back"
        self.ButtonBack["command"] = self.ActionButtonBack
        self.ButtonBack.pack( padx = 15 )

        self.Label = Label( self.Frame )
        self.Label["text"] = "Generations"
        self.Label["bg"] = "WHITE"
        self.Label["width"] = 15
        self.Label.pack( padx = 5, pady = 5, side = BOTTOM )

        self.LabelNumber = Label( self.Frame )
        self.LabelNumber["bg"] = "WHITE"
        self.LabelNumber["width"] = 15

    def ActionButtonBack( self ):

		self.Frame.destroy()
		self.RandMap.geometry( '350x145' )
		self.PCanvas.pack()

    def RunGameOfLife( self ):

        self.CanvasRandMap.delete('all')

        self.BitMatrix = []
        self.Matrix = Matrix(LineTotalSize, CollumnTotalSize, self.BitMatrix)
        self.Rules = ApplyRules( self.BitMatrix )
        self.Draw = DrawMatrix( self.BitMatrix, self.CanvasRandMap )

        self.NumGenerations = 0

        self.DefineInitialMatrix()

        while( True ):

            self.Draw.DrawMatrixFunction()

            self.LabelNumber["text"] = self.NumGenerations
            self.LabelNumber.pack( side = BOTTOM )

            self.RandMap.after( 50 )
            self.RandMap.update()

            self.LabelNumber.after( 50 )
            self.LabelNumber.update()

            self.NumGenerations += 1

            self.BitMatrix = self.Rules.ApplyRulesFunction()

            self.CanvasRandMap.delete('all')

    def DefineInitialMatrix( self ):

        for line in range( 1, LineTotalSize - 2 ):

            for collumn in range( 1, CollumnTotalSize - 2 ):

                if( randint( 0, 9 ) == 2 or randint( 0, 9 ) == 7 ):

                    self.Matrix.InsertElement( line, collumn, 1, self.BitMatrix )

                else:

                    self.Matrix.InsertElement( line, collumn, 0, self.BitMatrix )
