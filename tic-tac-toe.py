#!/usr/bin/env python3

class tic_tac_toe:

    def __init__(self, n):
        self.board = [ [ '' for i in range(n) ] for j in range(n) ]
        self.n = n
                      
    def print_board(self):
        for row in self.board:
            for c in row:
                print(c if len(c) == 1 else '-', end='')
            print()

    def play(self):
        curr_player = 1
        while True:
            curr_tic = 'X' if curr_player == 1 else 'O'
            inp = input("player " + str(curr_player) + " move: ")
            i, j = map(int, inp)
            if self.board[i][j] != '':
                continue
            self.board[i][j] = curr_tic

            if self.game_over(curr_tic):
                print("player " + str(curr_player) + " wins!!")
                break
            self.print_board()
            curr_player = int(not curr_player)

    def game_over(self, tic):
        if any(row ==  [tic]*self.n for row in self.board):
            return True

        for i in range(self.n):
            tot = 0
            for j in range(n):
                tot += 1 if self.board[j][i] == tic else 0
            if tot == self.n:
                return True

        i = j = tot = 0
        while i < self.n:
            tot += 1 if self.board[i][j] == tic else 0
            i+=1
            j+=1

        if tot == self.n:
            return True

        i = n-1
        j = tot = 0
        while j < self.n:
            tot += 1 if self.board[i][j] == tic else 0
            i-=1
            j+=1
            
if __name__ == '__main__':
    n = 3
    ttt = tic_tac_toe(n)
    ttt.play()
