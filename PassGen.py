import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip  

class PasswordGeneratorApp:
    def __init__(self, root):

        # initialize the app
        # parameters:
        # root (tk.Tk) => the root window of the application.

        self.root = root
        self.root.title("Password Generator")

        # label to prompt the user for the password length
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack()

        # entry widget for user to input the password length
        self.length_entry_widget = tk.Entry(root)
        self.length_entry_widget.pack()

        # button to trigger the password generation
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        # Button to copy the generated password to the clipboard
        self.copy_button = tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack()

    def generate_password(self):
        #Generate a random pass on user input and display.
        try:
            password_length = int(self.length_entry_widget.get())
            if password_length <= 0:
                raise ValueError
        except ValueError:
            # an error message if the num is not positive integer
            messagebox.showerror("Error", "Please enter a valid positive integer as password length.")
            return

        # Def character set for pass(letters, digits, and punctuation)
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate password based on random selecting of char from set
        generated_pass = ''.join(random.choice(characters) for _ in range(password_length))

        # Display the generated password in an information messagebox
        messagebox.showinfo("Generated Password", f"Your generated password is:\n{generated_pass}")

        # Save the generated password to a class variable for later use
        self.generated_pass = generated_pass

    def copy_to_clipboard(self):
        try:
            pyperclip.copy(self.generated_pass)
            messagebox.showinfo("Clipboard", "Password copied to clipboard!")
        except AttributeError:
            # pyperclip might not be available on all systems
            messagebox.showerror("Error", "Clipboard copy is not supported on your system.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    
    # start event loop
    root.mainloop()
