# Random Map Of Game of Life

from Tkinter import *
from random import *
from Matrix import *
from Common import *
from VarDefines import *

class ReadyMap:

    def __init__( self, Map, PreviousCanvas ):

        Map.geometry( '1335x650' )

        self.ReadyMap = Map
        self.PCanvas = PreviousCanvas

        self.Frame = Frame( self.ReadyMap )
        self.Frame["bg"] = "GRAY"
        self.Frame["bd"] = 1
        self.Frame.pack( side = LEFT )

        self.CanvasReadyMap = Canvas( self.Frame )
        self.CanvasReadyMap["bg"] = "GRAY"
        self.CanvasReadyMap["width"] = 1199
        self.CanvasReadyMap["heigh"] = 644
        self.CanvasReadyMap["highlightbackground"] = "WHITE"
        self.CanvasReadyMap.pack( side = LEFT )

        self.StdOne = Button( self.Frame )
        self.StdOne["bg"] = "WHITE"
        self.StdOne["highlightbackground"] = "BLACK"
        self.StdOne["bd"] = 0
        self.StdOne["width"] = 10
        self.StdOne["text"] = "Standard One"
        self.StdOne["command"] = self.StartStdOne
        self.StdOne.pack( padx = 15, pady = 20 )

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
		self.ReadyMap.geometry( '350x145' )
		self.PCanvas.pack()

    def StartStdOne( self ):

        self.CanvasReadyMap.delete('all')

        self.BitMatrix = []
        self.Matrix = Matrix(LineTotalSize, CollumnTotalSize, self.BitMatrix)
        self.Rules = ApplyRules( self.BitMatrix )
        self.Draw = DrawMatrix( self.BitMatrix, self.CanvasReadyMap )

        self.NumGenerations = 0

        self.DefineStandardOne()

        while( True ):

            self.Draw.DrawMatrixFunction()

            self.LabelNumber["text"] = self.NumGenerations
            self.LabelNumber.pack( side = BOTTOM )

            self.ReadyMap.after( 0 )
            self.ReadyMap.update()

            self.LabelNumber.after( 0 )
            self.LabelNumber.update()

            self.NumGenerations += 1

            self.BitMatrix = self.Rules.ApplyRulesFunction()

            self.CanvasReadyMap.delete('all')

    def DefineStandardOne( self ):

        for line in range( 1, LineTotalSize - 2 ):

            for collumn in range( 1, CollumnTotalSize - 2 ):

                    self.Matrix.InsertElement( line, collumn, 0, self.BitMatrix )

        self.Matrix.InsertElement( 5, 1, 1, self.BitMatrix )
        self.Matrix.InsertElement( 6, 1, 1, self.BitMatrix )
        self.Matrix.InsertElement( 5, 2, 1, self.BitMatrix )
        self.Matrix.InsertElement( 6, 2, 1, self.BitMatrix )

        self.Matrix.InsertElement( 5, 11, 1, self.BitMatrix )
        self.Matrix.InsertElement( 6, 11, 1, self.BitMatrix )
        self.Matrix.InsertElement( 7, 11, 1, self.BitMatrix )
        self.Matrix.InsertElement( 4, 12, 1, self.BitMatrix )
        self.Matrix.InsertElement( 8, 12, 1, self.BitMatrix )
        self.Matrix.InsertElement( 3, 13, 1, self.BitMatrix )
        self.Matrix.InsertElement( 9, 13, 1, self.BitMatrix )
        self.Matrix.InsertElement( 3, 14, 1, self.BitMatrix )
        self.Matrix.InsertElement( 9, 14, 1, self.BitMatrix )
        self.Matrix.InsertElement( 6, 15, 1, self.BitMatrix )
        self.Matrix.InsertElement( 4, 16, 1, self.BitMatrix )
        self.Matrix.InsertElement( 8, 16, 1, self.BitMatrix )
        self.Matrix.InsertElement( 5, 17, 1, self.BitMatrix )
        self.Matrix.InsertElement( 6, 17, 1, self.BitMatrix )
        self.Matrix.InsertElement( 7, 17, 1, self.BitMatrix )
        self.Matrix.InsertElement( 6, 18, 1, self.BitMatrix )

        self.Matrix.InsertElement( 3, 21, 1, self.BitMatrix )
        self.Matrix.InsertElement( 4, 21, 1, self.BitMatrix )
        self.Matrix.InsertElement( 5, 21, 1, self.BitMatrix )
        self.Matrix.InsertElement( 3, 22, 1, self.BitMatrix )
        self.Matrix.InsertElement( 4, 22, 1, self.BitMatrix )
        self.Matrix.InsertElement( 5, 22, 1, self.BitMatrix )
        self.Matrix.InsertElement( 2, 23, 1, self.BitMatrix )
        self.Matrix.InsertElement( 6, 23, 1, self.BitMatrix )
        self.Matrix.InsertElement( 1, 25, 1, self.BitMatrix )
        self.Matrix.InsertElement( 2, 25, 1, self.BitMatrix )
        self.Matrix.InsertElement( 6, 25, 1, self.BitMatrix )
        self.Matrix.InsertElement( 7, 25, 1, self.BitMatrix )

        self.Matrix.InsertElement( 3, 35, 1, self.BitMatrix )
        self.Matrix.InsertElement( 4, 35, 1, self.BitMatrix )
        self.Matrix.InsertElement( 3, 36, 1, self.BitMatrix )
        self.Matrix.InsertElement( 4, 36, 1, self.BitMatrix )
