import tkinter as tk
from tkinter import messagebox

def search_word(dictionary):
    def search():
        word = search_entry.get()
        if word in dictionary:
            meaning = ", ".join(dictionary[word])
            result_label.config(text=meaning)
        else:
            result_label.config(text="Word not found.")

    search_window = tk.Toplevel()
    search_window.title("Search Word")
    search_window.configure(bg="#333")
    search_frame = tk.Frame(search_window, bg="#333")
    search_frame.pack(padx=20, pady=20)
    search_label = tk.Label(search_frame, text="Enter word to search:", bg="#333", fg="white")
    search_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    search_entry = tk.Entry(search_frame, bg="#333", fg="white")
    search_entry.grid(row=0, column=1, padx=5, pady=5)
    search_button = tk.Button(search_frame, text="Search", command=search, width=15, bg="#555", fg="white")
    search_button.grid(row=1, column=0, columnspan=2, pady=10, sticky="we")
    result_label = tk.Label(search_window, text="", bg="#333", fg="white")
    result_label.pack(pady=10)
