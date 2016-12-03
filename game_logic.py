import random

#object for game logic so that it can be imported easily
class Game_logic:
    #constructor
    def __init__(self, num_rows, num_cols, symbols, colors):
        self.grid, self.answer_key = self.createGrid(num_rows, num_cols, symbols, colors)
        

    # creates a shuffled grid with num_cols number of columns that contains
    #    the first num_cols of symbols repeated num_rows times
    def createGrid(self, num_rows, num_cols, symbols, colors):
        duplicates = []

        # chooses num_row colors to randomly be assigned to each row
        color_list = list(colors)
        random.shuffle(color_list)

        # creates an array of symbols with unique color and symbol combinations
        for row in range(0, num_rows):
            color = color_list[row]
            for col in range(0, num_cols):
                duplicates.append(Symbol(color, symbols[col]))
        
        answer_key_prep = list(duplicates)
        random.shuffle(duplicates)

        shuffled_grid = []
        for col in range(0, num_cols):
            col = []
            for row in range(0, num_rows):
                col.append(duplicates.pop())
            shuffled_grid.append(col)

        answer_key = []
        for col in range(0, num_cols):
            col = []
            for row in range(0, num_rows):
                col.append(answer_key_prep.pop())
            answer_key.append(col)

        return (shuffled_grid, answer_key)

    def checkGrid(self):
        pass
                
            

    def swap(self, symbol_1, symbol_2):
        pass


class Symbol:
    def __init__(self, color, symbol):
        self.color = color
        self.symbol = symbol

    #def __str__(self):
    #   return self.symbol + " " + str(self.color)

        
