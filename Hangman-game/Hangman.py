class Hangman():    
    def __init__(self, word):
        self.word = word.lower()
        self.revealed = ["_"] * len(word)
        self.stage = 0
    
    def guess(self, letter):
        images = [
        """
        +---+
            |
            |
            |
            |
          =====
        """, 
        """
        +---+
        O   |
            |
            |
            |
          =====
        """,
        """
        +---+
        O   |
        |   |
            |
            |
          =====
        """,
        """
        +---+
        O   |
       /|   |
            |
            |
          =====
        """,
        """
        +---+
        O   |
       /|\  |
            |
            |
          =====
        """,
        """
        +---+
        O   |
       /|\  |
       /    |
            |
          =====
        """,
        """
        +---+
        O   |
       /|\  |
       / \  |
            |
          =====
        """
        ]

        wrong = True
        for i, char in enumerate(self.word):
            if char == letter:
                self.revealed[i] = char
                wrong = False

        if wrong:
            self.stage += 1
        
        print(images[self.stage])
        print(self.revealed)
    
    def is_over(self):
        return self.stage == 6 or "".join(self.revealed) == self.word
