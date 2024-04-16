# fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w"
# fen_to_board(fen)

pieces = ['r', 'n', 'b', 'q', 'k', 'p', 'R', 'N', 'B', 'Q', 'K', 'P']

def fen_to_board(fen):
    fen = fen.split(' ')[0]
    for i, char in enumerate(fen):
        if char in pieces:
            print(char, end="")
        elif char == '/': 
            print()
        else:
            for j in range(int(char)):
                print('.', end="")

if __name__ == '__main__':
    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w"
    fen_to_board(fen)