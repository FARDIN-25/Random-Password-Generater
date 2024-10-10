import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols, exclude_chars):
    character_set = ''
    
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation
    
    # Exclude specified characters
    character_set = ''.join(filter(lambda x: x not in exclude_chars, character_set))
    
    if not character_set:
        raise ValueError("No character set selected for password generation.")
    
    return ''.join(random.choice(character_set) for _ in range(length))

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        
        self.length_var = tk.IntVar(value=12)
        self.uppercase_var = tk.BooleanVar(value=True)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        self.exclude_chars_var = tk.StringVar()
        
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Password Length:").grid(column=0, row=0)
        ttk.Entry(self.root, textvariable=self.length_var).grid(column=1, row=0)
        
        ttk.Checkbutton(self.root, text="Include Uppercase", variable=self.uppercase_var).grid(column=0, row=1, sticky='W')
        ttk.Checkbutton(self.root, text="Include Lowercase", variable=self.lowercase_var).grid(column=0, row=2, sticky='W')
        ttk.Checkbutton(self.root, text="Include Numbers", variable=self.numbers_var).grid(column=0, row=3, sticky='W')
        ttk.Checkbutton(self.root, text="Include Symbols", variable=self.symbols_var).grid(column=0, row=4, sticky='W')

        ttk.Label(self.root, text="Exclude Characters:").grid(column=0, row=5)
        ttk.Entry(self.root, textvariable=self.exclude_chars_var).grid(column=1, row=5)

        self.generate_button = ttk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(column=0, row=6, columnspan=2)

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.grid(column=0, row=7, columnspan=2)

        self.copy_button = ttk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(column=0, row=8, columnspan=2)

    def generate_password(self):
        try:
            length = self.length_var.get()
            exclude_chars = self.exclude_chars_var.get()
            
            password = generate_password(
                length,
                self.uppercase_var.get(),
                self.lowercase_var.get(),
                self.numbers_var.get(),
                self.symbols_var.get(),
                exclude_chars
            )
            self.result_label.config(text=password)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def copy_to_clipboard(self):
        password = self.result_label.cget("text")
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

