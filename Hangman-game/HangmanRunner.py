from Hangman import Hangman

class HangmanRunner():
    def main():
        word = input("Enter the secret word. ")
        
        game = Hangman(word)
        print(game.revealed)
        
        
        while not game.is_over():
            g = input("Guess a letter.")
            game.guess(g)
        
        
        
            
    if __name__ == "__main__":
        main()