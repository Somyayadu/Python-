import tkinter as tk
import random
from tkinter import messagebox

# Generate random number
jackpot = random.randint(1, 100)
counter = 0

def check_guess():
    global counter
    guess = entry.get()
    if not guess.isdigit():
        messagebox.showwarning("Invalid Input", "Please enter a number between 1 and 100")
        return
    
    guess = int(guess)
    counter += 1
    
    if guess < jackpot:
        result_label.config(text="❌ Wrong! Try Higher ⬆️")
    elif guess > jackpot:
        result_label.config(text="❌ Wrong! Try Lower ⬇️")
    else:
        messagebox.showinfo("🎉 Congratulations!", f"✅ Correct Guess!\nAttempts: {counter}")
        root.destroy()

# Create window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x250")

# Title
title = tk.Label(root, text="🎲 Guess the Number (1–100)", font=("Arial", 14, "bold"))
title.pack(pady=10)

# Entry
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# Button
guess_button = tk.Button(root, text="Guess", font=("Arial", 12), command=check_guess)
guess_button.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run app
root.mainloop()
