# work with Matrix

class Matrix:

    def __init__( self, line, collumn, Matrix ):

        for self.line in range( 0, line ):

            MatrixLine = []

            for self.collumn in range( 0, collumn ):

                MatrixLine.append( -1 )

            Matrix.append( MatrixLine )

    def InsertElement( self, line, collumn, Element, Matrix ):

        Matrix[ line ][ collumn ] = Element

    def ShowMatrix( self, line, collumn, Matrix ):

        for lineTemp in range( 1, line - 2 ):
            print(Matrix[lineTemp])
            print("\n")
