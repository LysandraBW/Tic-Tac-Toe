WINNING_POSITIONS = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

BOARD_SPACES = 9

COLORS = {"H": '\033[94m', "R": '\033[91m', "END": '\033[0m'}


class Board:
    def __init__(self):
        self.board = [""] * 9
        self.winner = -1  # the index of the player
        self.moves = 0    # the number of total moves
        self.tie = False

    def display(self):
        print("\nBoard")

        space = 0

        while space < BOARD_SPACES:
            space_item = self.board[space]

            if space_item == "":
                print(str(space + 1), end="")
            else:
                print(COLORS[space_item] + space_item, end=COLORS["END"])

            space += 1

            if space >= BOARD_SPACES:
                print("\n")
                return

            if space % 3 == 0:
                print("\n---------")

            else:
                print(" | ", end="")

        print("\n")

    def add_move(self, player, space):
        if space < 1 or space > 9:
            return False
        if self.board[space - 1] != "":
            return False

        self.board[space - 1] = player.get_symbol()
        player.add_turn(space)
        self.moves += 1
        return True

    def update(self, player_one, player_two):
        for winning_position in WINNING_POSITIONS:
            if set(winning_position).issubset(set(player_one.get_turns())):
                self.winner = player_one.get_index()
                return True
            if set(winning_position).issubset(set(player_two.get_turns())):
                self.winner = player_two.get_index()
                return True

        if self.moves >= 9:
            self.tie = True
            return True

        return False

    def check_tie(self):
        return self.tie

    def check_win(self):
        return self.winner != -1, self.winner
