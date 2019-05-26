import random
import os
import string

from phrasehunter.phrase import Phrase


class Game:

    phrase_bank = ["Acura", "Alfa Romeo", "Aston Martin", "Audi", "Bentley", "BMW",
                   "Bugatti", "Buick", "Cadillac", "Chevrolet", "Chrysler", "Dodge",
                   "Ferrari", "Fiat", "Fisker", "Ford", "GMC", "Honda", "Hummer",
                   "Hyundai", "Infiniti", "Jaguar", "Jeep", "Kia", "Koenigsegg",
                   "Lamborghini", "Land Rover", "Lexus", "Lincoln", "Lotus", "Maserati"
                   "Maybach", "Mazda", "McLaren", "Mercedes Benz", "Mini", "Mitsubishi",
                   "Nissan", "Porsche", "Rolls Royce", "Spyker", "Subaru", "Tesla",
                   "Toyota", "Volkswagen", "Volvo"]
    active_phrase = []
    correct_answers = []
    player_answers = []
    lives = 5
    game_over = False
    play_game = True

    def __init__(self):
        """
        Pull and store a random phrase from the list of phrases stored in the class variable.

        The phrase is entered into a Phrase Object and stored into the random_phrase attributes.

        Loop through each letter in the selected phrase and store it in the class variable active_phrase.
        """
        self.phrase = random.choice(self.phrase_bank)
        self.random_phrase = Phrase(self.phrase)
        for letter in self.phrase:
            if not letter.isspace():
                self.active_phrase.append(letter.lower())

    def display_phrase(self):
        """
        Displays the phrase the user needs to guess against using the show_phrase
        method on the Phrase Object.
        """
        print("\n")
        return self.random_phrase.show_phrase()

    def reset(self):
        """
        Resets all previous game data if player decides to play again.
        """
        self.active_phrase.clear()
        self.correct_answers.clear()
        self.player_answers.clear()
        self.lives = 5
        self.game_over = False
        self.play_game = True
        self.phrase = random.choice(self.phrase_bank)
        self.random_phrase = Phrase(self.phrase)
        for letter in self.phrase:
            if not letter.isspace():
                self.active_phrase.append(letter.lower())

    def start_game(self):
        """ Starts game loop. """
        while self.play_game:
            self.display_phrase()
            self.player_input()
            self.win_loss()

    def player_input(self):
        """
        Tells user to guess a letter.

        If the user's guess is greater than 1, not a character between a-z, a guess they've put in before or
        more than 1 character the input isn't processed.

        If the user's input is valid the guess is store in class variable player_answers, the score is updated
        and if the guess is correct it is stored in class variable correct_answers.

        Once the method finishes the guess is checked against the Phrase Object check_character method.
        """
        player_guess = input("\n\nGuess a letter: ")
        if len(player_guess) > 1:
            self.clear_screen()
            print("\nYou can only enter 1 letter at a time. Try again.")
        elif player_guess not in string.ascii_lowercase:
            self.clear_screen()
            print("\nOnly letter guesses are allowed. Try again.")
        elif player_guess not in self.player_answers:
            self.clear_screen()
            self.player_answers.append(player_guess)
            self.update_score(player_guess)
            if player_guess in self.active_phrase:
                self.correct_answers.append(player_guess)
        else:
            self.clear_screen()
            print("\nYou've already guessed that letter. Guess again.")
        return self.random_phrase.check_character(player_guess)

    def update_score(self, player_guess):
        """
        Updates player's lives store in the class variable lives if a user's
        input is incorrect.
        """
        if player_guess not in self.active_phrase:
            self.lives -= 1
            self.clear_screen()
            print("\nWrong! You have {} out of 5 lives remaining!\n".format(self.lives))
            if self.lives == 0:
                self.game_over = True

    def win_loss(self):
        """ Checks whether a game is won or lost. """
        if self.game_over:
            self.clear_screen()
            user_input = input("\nGame Over. You ran out of lives! Would you like to play again? Y/N: ").lower()
            self.play_again(user_input)
        elif set(self.active_phrase) == set(self.correct_answers):
            self.clear_screen()
            self.display_phrase()
            user_input = input("\n\nYou Win! Would you like to play again? Y/N: ").lower()
            self.play_again(user_input)

    def play_again(self, user_input):
        """ Takes user's input to process if they would like to play again. """
        if user_input == "y" or user_input == "yes":
            self.clear_screen()
            self.reset()
            self.start_game()
        elif user_input == "n" or user_input == "no":
            self.clear_screen()
            print("\nGoodbye! Thank you for playing!")
            self.play_game = False
        else:
            self.clear_screen()
            print("\nI don't understand that! Goodbye! Thank you for playing!")
            self.play_game = False

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")
