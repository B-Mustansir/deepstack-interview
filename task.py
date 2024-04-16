def fen_to_board(fen):

    pieces = ['r', 'n', 'b', 'q', 'k', 'p', 'R', 'N', 'B', 'Q', 'K', 'P']
    
    fen_list = fen.split(' ')
    fen = fen_list[0]
    fen_player = fen_list[1]

    if fen_player == 'w':
        for i, char in enumerate(fen):
            if char.isalpha():
                print(char, end="")
            elif char == '/': 
                print()
            else:
                for j in range(int(char)):
                    print('.', end="")

    elif fen_player == 'b':
        fen = reversed(fen)
        for i, char in enumerate(fen):
            if char.isalpha():
                print(char, end="")
            elif char == '/': 
                print()
            else:
                for j in range(int(char)):
                    print('.', end="")        

if __name__ == '__main__':
    all_fens = ["rnbqkb1r/pp1p1ppp/5n2/1Np1p3/4P3/2NPBN2/PPP2PPP/R2QKB1R w KQkq - 0 7", "2r1r1k1/1p2qpbp/p2pp1p1/4n1N1/4P3/P2P1P2/1PQ1B1PP/R4RK1 w - - 0 1", "rn1q1rk1/p1p2ppp/1p1bbn2/3p4/3P1B2/2N1PN2/PP3PPP/R2Q1RK1 b - - 1 11", "8/8/2p3k1/2P1pp2/1p4p1/1P5p/1K6/8 w - - 1 56"]
    fen_to_board(all_fens[0])