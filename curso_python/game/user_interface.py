from tkinter import messagebox
from curso_python.game import engine
from functools import partial
import tkinter


#############################################################################################
class GameUI:

    def __init__(self):
        self.engine = engine.Engine()
        self.guess_entry = None
        self.player_name_field = None
        self.main_window = None

    def build(self):
        self.create_main_window()

    def check_guess(self, guess):
        # check guess
        self.engine.get_player_name(self.player_name_field.get())
        result_text = self.engine.play(guess=int(guess.get()))
        messagebox.showinfo("Result", result_text)

        # Closes main window if the secret number is correct
        if self.engine.secret_number == int(guess.get()):
            self.main_window.destroy()
            return

        self.reset_guess_field()

    def reset_guess_field(self):
        self.guess_entry.delete(0, 'end')

    def create_main_window(self):
        # Creates a main window
        window = tkinter.Tk()
        window.geometry("500x500")
        self.main_window = window

        # greeting text
        greeting = tkinter.Label(window, text="Guess the secret number!", font=("Helvetica", 18), pady=35)
        greeting.pack()

        # Instructions
        instruction_name = tkinter.Label(window, text="Guess the magic number between 1 and 30!",
                                         font=("Helvetica", 14),
                                         pady=10)
        instruction_name.pack()

        # name request
        name_label = tkinter.Label(window, text="Enter your name:", font=("Helvetica", 14), pady=10)
        name_label.pack()

        # player entry field
        player = tkinter.Entry(window)
        player.pack()
        self.player_name_field = player

        # name request
        guess = tkinter.Label(window, text="Try your luck!", font=("Helvetica", 14), pady=10)
        guess.pack()

        # guess entry field
        guess = tkinter.Entry(window)
        guess.pack()

        self.guess_entry = guess
        packed_function = partial(self.check_guess, guess)

        # submit button
        submit = tkinter.Button(window, text="Submit", padx=25, pady=25,
                                command=packed_function)  # check_guess, not check_guess()
        submit.pack()

        # Call show window
        window.mainloop()


#############################################################################################
GAME = GameUI()
GAME.build()
