class Chess:

    def __init__(self):

        battlefield = self.update_field(self.Figures)
        self.temporary_print(battlefield)
        pass
        # Field = [[0] * 8 for i in range(8)]

    class Figure:
        figure: str
        color: str
        pos_X: int
        pos_Y: int
        icon: str

        icons = {('Pawn', 'White'): '♙',
                 ('Queen', 'White'): '♕',
                 ('Rook', 'White'): '♖︎',
                 ('Bishop', 'White'): '♗',
                 ('Knight', 'White'): '♘︎',
                 ('King', 'White'): '♔︎',
                 ('Pawn', 'Black'): '♟︎',
                 ('Queen', 'Black'): '♛︎',
                 ('Rook', 'Black'): '♜︎',
                 ('Bishop', 'Black'): '♝︎',
                 ('Knight', 'Black'): '♞︎',
                 ('King', 'Black'): '♚︎'}

        def __init__(self, figure, color, pos_X, pos_Y):
            self.figure = figure
            self.color = color
            self.pos_X = pos_X
            self.pos_Y = pos_Y
            self.icon = self.icons[(figure, color)]

    def update_field(self, elements):
        field = [[0] * 8 for i in range(8)]
        for elem in elements:
            x_update = elem.pos_X
            y_update = elem.pos_Y
            field[x_update][y_update] = elem.icon
        return field

    def temporary_print(self, field):
        for line in field:
            print(*line)

    def move_pawn(self, pawn: Figure, New_X, New_Y):
        x = pawn.pos_X
        y = pawn.pos_y
        if x == New_X + 1 and y == New_Y:
            return True
        else:
            return False

    WPawn0 = Figure('Pawn', 'White', 1, 0)
    WPawn1 = Figure('Pawn', 'White', 1, 1)
    WPawn2 = Figure('Pawn', 'White', 1, 2)
    WPawn3 = Figure('Pawn', 'White', 1, 3)
    WPawn4 = Figure('Pawn', 'White', 1, 4)
    WPawn5 = Figure('Pawn', 'White', 1, 5)
    WPawn6 = Figure('Pawn', 'White', 1, 6)
    WPawn7 = Figure('Pawn', 'White', 1, 7)
    # _______________________________________________________________
    BPawn0 = Figure('Pawn', 'Black', 6, 0)
    BPawn1 = Figure('Pawn', 'Black', 6, 1)
    BPawn2 = Figure('Pawn', 'Black', 6, 2)
    BPawn3 = Figure('Pawn', 'Black', 6, 3)
    BPawn4 = Figure('Pawn', 'Black', 6, 4)
    BPawn5 = Figure('Pawn', 'Black', 6, 5)
    BPawn6 = Figure('Pawn', 'Black', 6, 6)
    BPawn7 = Figure('Pawn', 'Black', 6, 7)
    # _______________________________________________________________
    WRook0 = Figure('Rook', 'White', 0, 0)
    WRook1 = Figure('Rook', 'White', 0, 7)
    WKnight0 = Figure('Knight', 'White', 0, 1)
    WKnight1 = Figure('Knight', 'White', 0, 6)
    WBishop0 = Figure('Bishop', 'White', 0, 2)
    WBishop1 = Figure('Bishop', 'White', 0, 5)
    WKing = Figure('King', 'White', 0, 3)
    WQueen = Figure('Queen', 'White', 0, 4)
    # _______________________________________________________________
    BRook0 = Figure('Rook', 'Black', 7, 0)
    BRook1 = Figure('Rook', 'Black', 7, 7)
    BKnight0 = Figure('Knight', 'Black', 7, 1)
    BKnight1 = Figure('Knight', 'Black', 7, 6)
    BBishop0 = Figure('Bishop', 'Black', 7, 2)
    BBishop1 = Figure('Bishop', 'Black', 7, 5)
    BKing = Figure('King', 'Black', 7, 3)
    BQueen = Figure('Queen', 'Black', 7, 4)
    # _______________________________________________________________

    Figures = [WPawn0, WPawn1, WPawn2, WPawn3, WPawn4, WPawn5, WPawn6, WPawn7, BPawn7, BPawn6, BPawn5, BPawn4,
               BPawn3, BPawn2, BPawn1, BPawn0, WRook0, WRook1, WKnight1, WKnight0, WBishop0, WBishop1, WKing, WQueen,
               BRook1, BRook0, BBishop1, BBishop0, BKnight1, BKnight0, BKing, BQueen]


Chess()

