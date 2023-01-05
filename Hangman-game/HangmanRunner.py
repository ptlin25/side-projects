from Hangman import Hangman

class HangmanRunner():
    def main():
        word = input("Enter the secret word. ")
        
        game = Hangman(word)
        while not game.is_over:
            letter = input("Guess a letter. ")
            game.guess(letter)
        
            
    if __name__ == "__main__":
        main()