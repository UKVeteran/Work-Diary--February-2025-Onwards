import tkinter as tk
from tkinter import messagebox

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.turn = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        # Create the buttons for the grid
        for row in range(3):
            for col in range(3):
                button = tk.Button(root, text=" ", width=10, height=3, font=("Arial", 24),
                                   command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
        
        # Add a label for the current player's turn
        self.turn_label = tk.Label(root, text="Player X's turn", font=("Arial", 14))
        self.turn_label.grid(row=3, column=0, columnspan=3)
    
    def on_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.turn
            self.buttons[row][col].config(text=self.turn)

            if self.check_winner(self.turn):
                messagebox.showinfo("Game Over", f"Player {self.turn} wins!")
                self.reset_game()
                return

            if all(cell != " " for row in self.board for cell in row):
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
                return
            
            # Switch turns
            self.turn = "O" if self.turn == "X" else "X"
            self.turn_label.config(text=f"Player {self.turn}'s turn")
    
    def check_winner(self, player):
        # Check rows, columns, and diagonals
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True

        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def reset_game(self):
        # Reset the board and UI elements
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ")

        self.turn = "X"
        self.turn_label.config(text="Player X's turn")

# Create the main window
root = tk.Tk()

# Instantiate the game app
app = TicTacToeApp(root)

# Run the main event loop
root.mainloop()
