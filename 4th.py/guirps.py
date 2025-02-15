import tkinter as tk
import random

# Function to handle the game logic
def play(choice):
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    
    result_text.set(f"Computer chose: {computer_choice}")

    if choice == computer_choice:
        result_text.set(result_text.get() + "\nIt's a tie!")
    elif (choice == "rock" and computer_choice == "scissors") or \
         (choice == "scissors" and computer_choice == "paper") or \
         (choice == "paper" and computer_choice == "rock"):
        result_text.set(result_text.get() + "\nYou win!")
    else:
        result_text.set(result_text.get() + "\nYou lose!")

#GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.configure(bg="black")
root.geometry("300x200")

tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14)).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

rock_button = tk.Button(frame, text="Rock", font=("Arial", 12), command=lambda: play("rock"))
rock_button.pack(side=tk.LEFT, padx=5)

paper_button = tk.Button(frame, text="Paper", font=("Arial", 12), command=lambda: play("paper"))
paper_button.pack(side=tk.LEFT, padx=5)

scissors_button = tk.Button(frame, text="Scissors", font=("Arial", 12), command=lambda: play("scissors"))
scissors_button.pack(side=tk.LEFT, padx=5)

# results
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 14), fg="blue")
result_label.pack(pady=20)

# Start the GUI event loop
root.mainloop()