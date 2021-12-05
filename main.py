class Chess:

    def __init__(self):
        battlefield = self.update_field(self.Figures)
        self.print_battlefield(battlefield)
        # self.temporary_print(battlefield)

        move = 0
        while True:
            color = move % 2
            if color == 0:
                color = 'White'
            else:
                color = 'Black'
            print(color, 'move ->', end=' ')

            old_position, new_position = map(str, input().split(' '))

            (old_position, new_position) = ((self.Column.index(old_position[0]), int(old_position[1]) - 1),
                                            (self.Column.index(new_position[0]), int(new_position[1]) - 1))

            print(old_position, new_position, self.get_figure(old_position).icon)

            hero = self.get_figure(old_position)
            if self.check_move(hero, new_position, color):
                self.figure_update(hero, new_position)
                self.Figures[self.Figures.index(hero)] = hero
                move += 1
            else:
                print('Wrong move, repeat your move pls')

            battlefield = self.update_field(self.Figures)
            self.print_battlefield(battlefield)

        pass
        # Field = [[0] * 8 for i in range(8)]

    class Figure:
        figure: str
        color: str
        column: int
        line: int
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

        def __init__(self, figure, color, column, line):
            self.figure = figure
            self.color = color
            self.column = column
            self.line = line
            self.icon = self.icons[(figure, color)]

    def check_move(self, figure, position, color):
        name = figure.figure
        print(name)
        old_position = (figure.column, figure.line)
        output = False
        if name == 'Pawn':
            if color == 'White':
                output = self.move_pawn_white(figure, position[0], position[1])
                output = output and self.white_pawn_check_ahead(figure, position[0], position[1])
                output = output or self.check_first_move_white(figure, position[0], position[1])
                output = output or self.white_pawn_can_eat(figure, position[0], position[1])

                if self.white_pawn_can_eat(figure, position[0], position[1]):
                    to_delete = self.get_figure((position[0], position[1]))
                    self.Figures.remove(to_delete)
            else:
                output = self.move_pawn_black(figure, position[0], position[1])
                output = output and self.black_pawn_check_ahead(figure, position[0], position[1])
                # print(output)
                output = output or self.check_first_move_black(figure, position[0], position[1])
                # print(output)
                output = output or self.black_pawn_can_eat(figure, position[0], position[1])
                # print(output)

                # print(output)
                if self.black_pawn_can_eat(figure, position[0], position[1]):
                    to_delete = self.get_figure((position[0], position[1]))
                    self.Figures.remove(to_delete)

        return output

    def get_figure(self, position):
        for elem in self.Figures:
            check = (elem.column, elem.line)
            if check == position:
                return elem

    def figure_update(self, figure, position):
        figure.column = position[0]
        figure.line = position[1]

    def update_field(self, elements):
        # python reads line - column, but you need column - line, so reverse
        field = [[0] * 8 for i in range(8)]
        for elem in elements:
            x_update = elem.column
            y_update = elem.line
            field[y_update][x_update] = elem.icon
        return field

    def temporary_print(self, field):
        for line in field:
            print(*line)

    # Check move _____________________________________________________________________________________________________

    def white_pawn_check_ahead(self, pawn: Figure, New_X, New_Y):
        if pawn.column == New_X and (pawn.line + 1 == New_Y or pawn.line + 2 == New_Y):
            for elem in self.Figures:
                if New_X == elem.column and New_Y == elem.line:
                    return False
            else:
                return True
        else:
            return False

    def move_pawn_white(self, pawn: Figure, New_X, New_Y):
        column = pawn.column
        line = pawn.line
        #print((column, line), (New_X, New_Y))
        if (column == New_X) and (line + 1 == New_Y):
            return True
        else:
            return False

    def check_first_move_white(self, pawn: Figure, New_X, New_Y):
        line = pawn.line
        column = pawn.column
        if line == 1:
            if column == New_X and line + 2 == New_Y:
                return True
            else:
                return False
        else:
            return False

    def white_pawn_can_eat(self, pawn: Figure, New_X, New_Y):
        is_standing_on = False
        column = pawn.column
        line = pawn.line
        for element in self.Figures:
            if (element.column, element.line) == (New_X, New_Y):
                is_standing_on = True
        if column + 1 == New_X or column - 1 == New_X:
            if line + 1 == New_Y and is_standing_on:
                return True
            else:
                return False
        else:
            return False

    def black_pawn_check_ahead(self, pawn: Figure, New_X, New_Y):
        if pawn.column == New_X and (pawn.line - 1 == New_Y or pawn.line - 2 == New_Y):
            for elem in self.Figures:
                if New_X == elem.column and New_Y == elem.line:
                    return False
            else:
                return True
        else:
            return False

    def move_pawn_black(self, pawn: Figure, New_X, New_Y):
        column = pawn.column
        line = pawn.line
        #print((column, line), (New_X, New_Y))
        if (column == New_X) and (line - 1 == New_Y):
            return True
        else:
            return False

    def check_first_move_black(self, pawn: Figure, New_X, New_Y):
        line = pawn.line
        column = pawn.column
        if line == 6:
            if column == New_X and line - 2 == New_Y:
                return True
            else:
                return False
        else:
            return False

    def black_pawn_can_eat(self, pawn: Figure, New_X, New_Y):
        is_standing_on = False
        column = pawn.column
        line = pawn.line
        for element in self.Figures:
            if (element.column, element.line) == (New_X, New_Y):
                is_standing_on = True
        if column - 1 == New_X or column + 1 == New_X:
            if line - 1 == New_Y and is_standing_on:
                return True
            else:
                return False
        else:
            return False

    # Print __________________________________________________________________________________________________________

    def print_battlefield(self, field):
        print(' ', end='')
        for elem in self.Column:
            print(elem, end='    ')
        print(' ')
        for line in field:
            print('|', end=' ')
            for elem in line:
                printing = elem
                if printing == 0:
                    printing = '⠀ '

                print(printing, end=' | ')
            print(' ')
            print('-------------------------------------')
        print(' ')

    WPawn0 = Figure('Pawn', 'White', 0, 1)
    WPawn1 = Figure('Pawn', 'White', 1, 1)
    WPawn2 = Figure('Pawn', 'White', 2, 1)
    WPawn3 = Figure('Pawn', 'White', 3, 1)
    WPawn4 = Figure('Pawn', 'White', 4, 1)
    WPawn5 = Figure('Pawn', 'White', 5, 1)
    WPawn6 = Figure('Pawn', 'White', 6, 1)
    WPawn7 = Figure('Pawn', 'White', 7, 1)
    # _______________________________________________________________
    BPawn0 = Figure('Pawn', 'Black', 0, 6)
    BPawn1 = Figure('Pawn', 'Black', 1, 6)
    BPawn2 = Figure('Pawn', 'Black', 2, 6)
    BPawn3 = Figure('Pawn', 'Black', 3, 6)
    BPawn4 = Figure('Pawn', 'Black', 4, 6)
    BPawn5 = Figure('Pawn', 'Black', 5, 6)
    BPawn6 = Figure('Pawn', 'Black', 6, 6)
    BPawn7 = Figure('Pawn', 'Black', 7, 6)
    # _______________________________________________________________
    WRook0 = Figure('Rook', 'White', 0, 0)
    WRook1 = Figure('Rook', 'White', 7, 0)
    WKnight0 = Figure('Knight', 'White', 1, 0)
    WKnight1 = Figure('Knight', 'White', 6, 0)
    WBishop0 = Figure('Bishop', 'White', 2, 0)
    WBishop1 = Figure('Bishop', 'White', 5, 0)
    WKing = Figure('King', 'White', 3, 0)
    WQueen = Figure('Queen', 'White', 4, 0)
    # _______________________________________________________________
    BRook0 = Figure('Rook', 'Black', 0, 7)
    BRook1 = Figure('Rook', 'Black', 7, 7)
    BKnight0 = Figure('Knight', 'Black', 1, 7)
    BKnight1 = Figure('Knight', 'Black', 6, 7)
    BBishop0 = Figure('Bishop', 'Black', 2, 7)
    BBishop1 = Figure('Bishop', 'Black', 5, 7)
    BKing = Figure('King', 'Black', 3, 7)
    BQueen = Figure('Queen', 'Black', 4, 7)
    # _______________________________________________________________

    Figures = [WPawn0, WPawn1, WPawn2, WPawn3, WPawn4, WPawn5, WPawn6, WPawn7, BPawn7, BPawn6, BPawn5, BPawn4,
               BPawn3, BPawn2, BPawn1, BPawn0, WRook0, WRook1, WKnight1, WKnight0, WBishop0, WBishop1, WKing, WQueen,
               BRook1, BRook0, BBishop1, BBishop0, BKnight1, BKnight0, BKing, BQueen]

    Column = 'ABCDEFGH'


Chess()