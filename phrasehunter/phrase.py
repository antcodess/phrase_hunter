from phrasehunter.character import Character


class Phrase:

    def __init__(self, phrase):
        """
        Takes an incoming phrase and stores it into the phrase attribute.
        Creates the letters attribute as an empty list and loops over the characters self.phrase
        and calls the Character Object with each letter as the argument.
        """
        self.phrase = phrase
        self.letters = []
        for letter in self.phrase:
            self.letters.append(Character(letter))

    def check_character(self, guess):
        """
        Takes a users guess and checks the guess against a Character instance
        using it's method check_guess.
        """
        for character in self.letters:
            character.check_guess(guess)

    def show_phrase(self):
        """ Shows characters on screen using Character class method show_character. """
        for character in self.letters:
            print(character.show_character(), end=" ")
