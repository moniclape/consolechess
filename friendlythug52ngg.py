import random

class сhess:
    def __init__(gg):
        gg.board = [
            [".", "n", "g", "q", "k", "g", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "G", "Q", "K", "G", "N", "."]
        ]
        gg.turn = "white"

    def display_board(gg):
        print(" ")
        print("  a b c d e f g h")
        print("  ----------------")
        for i in range(8):
            print(8 - i, end="|")
            for j in range(8):
                print(gg.board[i][j], end=" ")
            print("|", 8 - i)
        print("  ----------------")
        print("  a b c d e f g h")
        print(" ")

    def pawn_move(gg, piece, sr, sc, er, ec):
        if piece == "P":
            if er == sr - 1 and sc == ec and gg.board[er][ec] == ".":
                return True
            if sr == 6 and er == sr - 2 and sc == ec and gg.board[er][ec] == "." and gg.board[sr - 1][sc] == ".":
                return True
            if er == sr - 1 and abs(ec - sc) == 1 and gg.board[er][ec].islower() and gg.board[er][ec].islower() != 'r':
                return True
            if er == 0 and gg.board[er][ec] == ".":
                which_piece = str(input("The white pawn in the end of the board, choose the piece you want to become (Q, G, N): "))
                if which_piece == 'Q':
                    gg.board[er][ec] = 'Q'
                elif which_piece == 'G':
                    gg.board[er][ec] = 'G'
                elif which_piece == 'N':
                    gg.board[er][ec] = 'N'
                return True 
        if piece == "p":
            if er == sr + 1 and sc == ec and gg.board[er][ec] == ".":
                return True
            if sr == 1 and er == sr + 2 and sc == ec and gg.board[er][ec] == "." and gg.board[sr + 1][sc] == ".":
                return True
            if er == sr + 1 and abs(ec - sc) == 1 and gg.board[er][ec].isupper() and gg.board[er][ec].islower() != 'r':
                return True
            if er == 7 and gg.board[er][ec] == ".":
                which_piece = str(input("The black pawn in the end of the board, choose the piece you want to become (q, g, n): "))
                if which_piece == 'q':
                    gg.board[er][ec] = 'q'
                elif which_piece == 'g':
                    gg.board[er][ec] = 'g'
                elif which_piece == 'n':
                    gg.board[er][ec] = 'n'
                return True 
        return False 


    def ruin_move(gg, start_row, start_col, end_row, end_col):
        if (end_row + end_col) % 2 != 0 and gg.board[end_row][end_col] == '.':
            return True
        return False

    def knight_move(gg, sr, sc, er, ec):
        row_diff = abs(er - sr)
        col_diff = abs(ec - sc)
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            target_piece = gg.board[er][ec]
            if (gg.turn == "white" and (target_piece == "." or target_piece.islower())) or (gg.turn == "black" and (target_piece == "." or target_piece.isupper())) and gg.board[er][ec].islower() != 'r':
                return True
        return False


    def queen_move(gg, sr, sc, er, ec):
        if sr == er or sc == ec:
            if sr != er and sc != ec:
                return False
            if sr == er:
                step = 1 if ec > sc else -1
                for col in range(sc + step, ec, step):
                    if gg.board[sr][col] != ".":
                        return False
            else:
                step = 1 if er > sr else -1
                for row in range(sr + step, er, step):
                    if gg.board[row][sc] != ".":
                        return False
            target_piece = gg.board[er][ec]
            if (gg.turn == "white" and (target_piece == "." or target_piece.islower())) or (gg.turn == "black" and (target_piece == "." or target_piece.isupper())) and gg.board[er][ec].islower() != 'r':
                return True
            return False
        elif abs(er - sr) == abs(ec - sc):
            step_row = 1 if er > sr else -1
            step_col = 1 if ec > sc else -1
            row, col = sr + step_row, sc + step_col
            while (row != er) and (col != ec):
                if gg.board[row][col] != ".":
                    return False
                row += step_row
                col += step_col
            target_piece = gg.board[er][ec]
            if (gg.turn == "white" and (target_piece == "." or target_piece.islower())) or (gg.turn == "black" and (target_piece == "." or target_piece.isupper())) and gg.board[er][ec].islower() != 'r':
                return True
        return False


    def king_move(gg, sr, sc, er, ec):
        row_diff = abs(er - sr)
        col_diff = abs(ec - sc)
        if row_diff <= 1 and col_diff <= 1:
            target_piece = gg.board[er][ec]
            if (gg.turn == "white" and (target_piece == "." or target_piece.islower())) or (gg.turn == "black" and (target_piece == "." or target_piece.isupper())) and gg.board[er][ec].islower() != 'r':
                return True
        return False


    def goose_move(gg, piece, sr, sc, er, ec):
        if piece == "G":
            if (er == sr - 1 and ec in [sc - 1, sc + 1]) or (er == sr - 2 and sc == ec and gg.board[er][ec] == ".") or (er == sr and ec in [sc - 2, sc + 2]):
                return True
        elif piece == "g":
            if (er == sr + 1 and ec in [sc - 1, sc + 1]) or (er == sr + 2 and sc == ec and gg.board[er][ec] == ".") or (er == sr and ec in [sc - 2, sc + 2]):
                return True
        return False

    def move_goose(gg, sr, sc, er, ec):
        if gg.goose_move(gg.board[sr][sc], sr, sc, er, ec):
            if sr - er == 0 and sc - ec == 2:
                target_piece = gg.board[er][ec + 1]
            elif sr - er == 2 and sc - ec == 0:
                target_piece = gg.board[er + 1][ec]
            elif sr - er == 0 and sc - ec == -2:
                target_piece = gg.board[er][ec - 1]
            else:
                target_piece = "."

            if target_piece != ".":
                randnum = random.randint(1, 10)
                print("Random number:", randnum)
                if randnum % 2 == 0:  
                    print(f"{gg.board[sr][sc]} kills {target_piece}.")
                    gg.board[er][ec] = gg.board[sr][sc]
                    gg.board[sr][sc] = "."
                else:
                    print("Number is odd!")
                    gg.board[er][ec] = gg.board[sr][sc]
                    gg.board[sr][sc] = "."
            else:
                gg.board[er][ec] = gg.board[sr][sc]
                gg.board[sr][sc] = "."
            return True
        return False    

    def make_move(gg, sr, sc, er, ec):
        piece = gg.board[sr][sc]
        gg.board[er][ec] = piece
        gg.board[sr][sc] = "."
        return True


    def move_piece(gg, sr, sc, er, ec):
        piece = gg.board[sr][sc]
        if piece.lower() == "p":
            if gg.pawn_move(piece, sr, sc, er, ec):
                return gg.make_move(sr, sc, er, ec)
        elif piece.lower() == "r":
            if gg.ruin_move(sr, sc, er, ec):
                return gg.make_move(sr, sc, er, ec)
        elif piece.lower() == "n":
            if gg.knight_move(sr, sc, er, ec):
                return gg.make_move(sr, sc, er, ec)
        elif piece.lower() == "q":
            if gg.queen_move(sr, sc, er, ec):
                return gg.make_move(sr, sc, er, ec)
        elif piece.lower() == "k":
            if gg.king_move(sr, sc, er, ec):
                return gg.make_move(sr, sc, er, ec)
        elif piece.lower() == "g":
            if gg.move_goose(sr, sc, er, ec):
                return True
        return False     

    def check_king_alive(gg, turn):
        if turn == 'white':
            for i in range(8):
                if 'k' in gg.board[i]:
                    return True
            return False
        if turn == 'black':
            for i in range(8):
                if 'K' in gg.board[i]:
                    return True
            return False

    def play_game(gg):
        game_count = 0
        while True:
            if gg.check_king_alive(gg.turn) == False:
                print(f"{gg.turn} win!")
                break
            gg.display_board()
            print(f"Turn {gg.turn}")
            print(f"Game moves - {game_count}")
            move = input("type a notation (e2 e4): ")
            if len(move.split()) != 2:
                print("Incorrect move, type like this - 'e2 e4'.")
                continue
            start, end = move.split()
            start_col = ord(start[0]) - ord('a')
            start_row = 8 - int(start[1])
            end_col = ord(end[0]) - ord('a')
            end_row = 8 - int(end[1])
            if gg.move_piece(start_row, start_col, end_row, end_col):
                gg.turn = "black" if gg.turn == "white" else "white"
                game_count += 1
            else:
                print("Incorrect move, try again:")

x = сhess()
x.play_game()
