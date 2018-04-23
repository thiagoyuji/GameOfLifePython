# Users Draw in Window

from Tkinter import *
from Matrix import *
from Common import *
from VarDefines import *

class DrawMap:

    def __init__( self, Map, PreviousCanvas ):

        Map.geometry( '1335x650' )

        self.DrawMap = Map
        self.PCanvas = PreviousCanvas

        self.Frame = Frame( self.DrawMap )
        self.Frame["bg"] = "GRAY"
        self.Frame["bd"] = 1
        self.Frame.pack( side = LEFT )

        self.CanvasDrawMap = Canvas( self.Frame )
        self.CanvasDrawMap["bg"] = "GRAY"
        self.CanvasDrawMap["width"] = 1199
        self.CanvasDrawMap["heigh"] = 644
        self.CanvasDrawMap["highlightbackground"] = "WHITE"
        self.CanvasDrawMap.create_text(100,40, text='Press Draw and Start to Play', fill='BLACK')
        self.CanvasDrawMap.pack( side = LEFT )

        self.ButtonDraw = Button( self.Frame )
        self.ButtonDraw["bg"] = "WHITE"
        self.ButtonDraw["highlightbackground"] = "BLACK"
        self.ButtonDraw["bd"] = 0
        self.ButtonDraw["width"] = 10
        self.ButtonDraw["text"] = "Draw"
        self.ButtonDraw["command"] = self.RunDrawMap
        self.ButtonDraw.pack( padx = 15, pady = 5 )

        self.ButtonStart = Button( self.Frame )
        self.ButtonStart["bg"] = "WHITE"
        self.ButtonStart["highlightbackground"] = "BLACK"
        self.ButtonStart["bd"] = 0
        self.ButtonStart["width"] = 10
        self.ButtonStart["text"] = "Start"
        self.ButtonStart.pack( padx = 15, pady = 5 )

        self.ButtonBack = Button( self.Frame )
        self.ButtonBack["bg"] = "WHITE"
        self.ButtonBack["highlightbackground"] = "BLACK"
        self.ButtonBack["bd"] = 0
        self.ButtonBack["width"] = 10
        self.ButtonBack["text"] = "Back"
        self.ButtonBack["command"] = self.ActionButtonBack
        self.ButtonBack.pack( padx = 15, pady = 5 )

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
		self.DrawMap.geometry( '350x145' )
		self.PCanvas.pack()

    def RunDrawMap( self ):

        self.CanvasDrawMap.delete('all')

        self.BitMatrix = []
        self.Matrix = Matrix(LineTotalSize, CollumnTotalSize, self.BitMatrix)
        self.Rules = ApplyRules( self.BitMatrix )
        self.Draw = DrawMatrix( self.BitMatrix, self.CanvasDrawMap )

        self.NumGenerations = 0

        self.ButtonStart["command"] = self.RunGameOfLife

        self.DefineNullMatrix()

        while( True ):

            self.Draw.DrawMatrixFunction()

            self.CanvasDrawMap.update()

            self.DefineInitialMatrixByUser()

            self.CanvasDrawMap.delete('all')

    def RunGameOfLife( self ):

        while( True ):

            self.Draw.DrawMatrixFunction()

            self.LabelNumber["text"] = self.NumGenerations
            self.LabelNumber.pack( side = BOTTOM )

            self.DrawMap.after( 50 )
            self.DrawMap.update()

            self.LabelNumber.after( 50 )
            self.LabelNumber.update()

            self.NumGenerations += 1

            self.BitMatrix = self.Rules.ApplyRulesFunction()

            self.CanvasDrawMap.delete('all')

    def DefineNullMatrix( self ):

        for line in range( 1, LineTotalSize - 2 ):
            for collumn in range( 1, CollumnTotalSize - 2 ):

                    self.Matrix.InsertElement( line, collumn, 0, self.BitMatrix )

    def DefineInitialMatrixByUser( self ):

        self.CanvasDrawMap.bind('<Button-1>', self.PutAliceCellInMatrix)

    def PutAliceCellInMatrix( self, Event ):

        controller = 15

        line = 1
        collumn = 1

        while( controller < Event.y ):

            line += 1
            controller += 15

        controller = 15

        while( controller < Event.x ):

            collumn += 1
            controller +=15

        self.Matrix.InsertElement( line, collumn, 1, self.BitMatrix )
