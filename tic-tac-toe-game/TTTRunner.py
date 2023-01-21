from TicTacToe import TicTacToe

class TTTRunner:
    def main():
        
        game = TicTacToe()
        turn = 0
        
        while turn < 9 and game.winner() is None:
            turn += 1
            if turn % 2 == 1:
                player = 1
            else:
                player = 2
            game.turn(player)
        if turn == 9:
            print("Tie")
        else:
            print(game.winner() + " wins!")
        
    if __name__ == "__main__":
        main()