import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("350x250")
        self.root.resizable(False, False)

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(root, text="Guess a number between 1 and 100:", font=('Arial', 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=('Arial', 12))
        self.entry.pack()

        self.result_label = tk.Label(root, text="", font=('Arial', 12), fg="blue")
        self.result_label.pack(pady=10)

        self.button = tk.Button(root, text="Submit Guess", font=('Arial', 12), command=self.check_guess)
        self.button.pack(pady=5)

        self.restart_button = tk.Button(root, text="Restart Game", font=('Arial', 12), command=self.restart_game)
        self.restart_button.pack(pady=5)
        self.restart_button.config(state="disabled")

    def check_guess(self):
        guess = self.entry.get()

        if not guess.isdigit():
            self.result_label.config(text=" Please enter a valid number.")
            return

        guess = int(guess)
        self.attempts += 1

        if guess < self.secret_number:
            self.result_label.config(text=" Too low! Try again.")
        elif guess > self.secret_number:
            self.result_label.config(text=" Too high! Try again.")
        else:
            self.result_label.config(
                text=f" Correct! You guessed it in {self.attempts} tries.")
            self.button.config(state="disabled")
            self.restart_button.config(state="normal")

    def restart_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.button.config(state="normal")
        self.restart_button.config(state="disabled")


# Create main window
root = tk.Tk()
game = NumberGuessingGame(root)
root.mainloop()
