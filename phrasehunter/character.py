class Character:

    def __init__(self, original, was_guessed=False):
        """ Checks if the original parameter is only 1 character. """
        if len(original) > 1:
            raise ValueError("Object can only accept 1 character")
        self.original = original
        self.was_guessed = was_guessed
        self.hidden_guess = "_"

    def check_guess(self, guess):
        """ Checks if a guess is the same as the original attribute. """
        if guess.lower() == self.original.lower():
            self.was_guessed = True

    def show_character(self):
        """
        Returns the original attribute or hidden_guess attribute when called.
        """
        if self.was_guessed or self.original.isspace():
            return self.original
        else:
            return self.hidden_guess
