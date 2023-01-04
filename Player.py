class Player:
    MAX_TURNS = 5

    def __init__(self, symbol, index):
        self.symbol = symbol  # symbol used on the board
        self.index = index    # index in the "players" array (TicTacToe.py)
        self.turns = [0] * self.MAX_TURNS
        self.turn_count = 0

    def add_turn(self, turn):
        if self.turn_count >= self.MAX_TURNS:
            return

        self.turns[self.turn_count] = turn
        self.turn_count += 1

    def get_symbol(self):
        return self.symbol

    def get_turns(self):
        return self.turns

    def get_index(self):
        return self.index
