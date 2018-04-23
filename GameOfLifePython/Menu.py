# Menu Of the Game
    # This menu use the GUI Tkinter

from Tkinter import *
from RandomMap import *
from ReadyMap import *
from DrawMap import *

class Menu:

    def __init__( self ):

        self.Menu = Tk()
        self.Menu.title( "Game of Life" )
        self.Menu.geometry( '350x145' )
        self.Menu.resizable( False, False )
        self.Menu["bg"] = "GRAY"

        self.Canvas = Canvas( self.Menu )
        self.Canvas["bg"] = "GRAY"
        self.Canvas["highlightbackground"] = "BLACK"
        self.Canvas.pack()

        self.ButtonStdRandom = Button( self.Canvas )
        self.ButtonStdRandom["bg"] = "WHITE"
        self.ButtonStdRandom["highlightbackground"] = "BLACK"
        self.ButtonStdRandom["bd"] = 0
        self.ButtonStdRandom["width"] = 20
        self.ButtonStdRandom["text"] = "Standard Random"
        self.ButtonStdRandom["command"] = self.ActionStandardRandom
        self.ButtonStdRandom.place( x = 30, y = 30 )

        self.ButtonStdReady = Button( self.Canvas )
        self.ButtonStdReady["bg"] = "WHITE"
        self.ButtonStdReady["highlightbackground"] = "BLACK"
        self.ButtonStdReady["bd"] = 0
        self.ButtonStdReady["width"] = 20
        self.ButtonStdReady["text"] = "Standard Ready"
        self.ButtonStdReady["command"] = self.ActionStandardReady
        self.ButtonStdReady.place( x = 30, y = 60 )

        self.ButtonStsDraw = Button( self.Canvas )
        self.ButtonStsDraw["bg"] = "WHITE"
        self.ButtonStsDraw["highlightbackground"] = "BLACK"
        self.ButtonStsDraw["bd"] = 0
        self.ButtonStsDraw["width"] = 20
        self.ButtonStsDraw["text"] = "Standard Draw"
        self.ButtonStsDraw["command"] = self.ActionStandardDraw
        self.ButtonStsDraw.place( x = 30, y = 90 )

        self.Menu.mainloop()

    def ActionStandardRandom( self ):

        self.Canvas.pack_forget()

        __RandMap = RandomMap( self.Menu, self.Canvas )
        __RandMap.mainloop()

    def ActionStandardReady( self ):

        self.Canvas.pack_forget()

        __ReadyMap = ReadyMap( self.Menu, self.Canvas )
        __ReadyMap.mainloop()

    def ActionStandardDraw( self ):

        self.Canvas.pack_forget()

        __DrawMap = DrawMap( self.Menu, self.Canvas )
        __DrawMap.mainloop()
