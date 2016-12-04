import random

#object for game logic so that it can be imported easily
class GridManager:
    #constructor
    def __init__(self, num_rows, num_cols, symbols, colors):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.grid = self.createGrid(num_rows, num_cols, symbols, colors)
        self.score = num_rows * num_cols
        

    # creates a shuffled grid with num_cols number of columns that contains
    #    the first num_cols of symbols repeated num_rows times
    def createGrid(self, num_rows, num_cols, symbols, colors):
        duplicates = []
		
        symbol_list = list(symbols)
        random.shuffle(symbol_list)

        # chooses num_row colors to randomly be assigned to each row
        color_list = list(colors)
        random.shuffle(color_list)

        # creates an array of symbols with unique color and symbol combinations
        for row in range(0, num_rows):
            color = color_list[row]
            for col in range(0, num_cols):
                duplicates.append(Symbol(color, symbol_list[col]))
        
        random.shuffle(duplicates)

        # creates a shuffled grid
        shuffled_grid = []
        for col in range(0, num_cols):
            col = []
            for row in range(0, num_rows):
                col.append(duplicates.pop())
            shuffled_grid.append(col)

        # returns the shuffled grid 
        return shuffled_grid

    # returns true if the player's grid is the same as the answer key
    def gridIsSolved(self):
        # get the symbols from each col
        for row in range(0, self.num_rows):
            symbol_check = []
            for col in range(0, self.num_cols):
                symbol_check.append(self.grid[col, row].symbol)

            #check the symbols in each col and make sure they are the same
            symbol = symbol_check[0]
            for s in symbol_check:
                if s != symbol:
                    return False

        # get the colors from each row
        for col in range(0, self.num_cols):
            color_check = []
            for row in range(0, self.num_rows):
                color_check.append(self.grid[col, row].color)

            #check the colors in each row and make sure they are the same
            color = color_check[0]
            for c in color_check:
                if c!= color:
                    return False

        # all the rows have the same color and all of the cols have the same symbol
        return True

    # swaps the location of two items on the grid            
    def swap(self, symbol_1, symbol_2):
        index_of_1 = self.getIndexOf(symbol_1)
        index_of_2 = self.getIndexOf(symbol_2)
        if index_of_1 != (-1, -1) and index_of_2 != (-1, -1):
            col1, row1 = index_of_1
            self.grid[col1].insert(row1, symbol_2)
            self.grid[col1].remove(symbol_1)

            col2, row2 = index_of_2
            self.grid[col2].insert(row2, symbol_1)
            self.grid[col2].remove(symbol_2)
        self.score--

    # returns the location of the given symbol as a tuple.
    #   if symbol is not found, returns (-1, -1)
    def getIndexOf(self, symbol):
        for col in range(0, self.num_cols):
            for row in range(0, self.num_rows):
                if self.grid[col][row] == symbol:
                    return (col, row)
        return (-1, -1)
    
class Symbol:
    def __init__(self, color, symbol):
        self.color = color
        self.symbol = symbol        
