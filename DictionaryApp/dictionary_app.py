import tkinter as tk
from tkinter import ttk
from dictionary_operations import add_word, delete_word
from dictionary_data import load_dictionary, save_dictionary
from dictionary_search import search_word
from test_yourself import test_yourself

root = tk.Tk()
root.title("Dictionary Application")
root.geometry("600x575")
root.configure(bg="#333")

frame = tk.Frame(root, bg="#333")
frame.pack(pady=20)

word_label = tk.Label(frame, text="Word:", bg="#333", fg="white")
word_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
word_entry = tk.Entry(frame, bg="#333", fg="white")
word_entry.grid(row=0, column=1, padx=5, pady=5)

meaning_label = tk.Label(frame, text="Meaning:", bg="#333", fg="white")
meaning_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
meaning_entry = tk.Entry(frame, bg="#333", fg="white")
meaning_entry.grid(row=1, column=1, padx=5, pady=5)

add_button = tk.Button(frame, text="Add Word", command=lambda: add_word(dictionary, tree, word_entry.get(), meaning_entry.get()), bg="#555", fg="white")
add_button.grid(row=2, column=0, columnspan=2, pady=10, sticky="we")

tree_frame = tk.Frame(root, bg="#333")
tree_frame.pack(pady=20)
tree = ttk.Treeview(tree_frame, columns=("Word", "Meaning"), show="headings", style="Custom.Treeview")
tree.heading("Word", text="Word")
tree.heading("Meaning", text="Meaning")
tree.pack(side="left")

style = ttk.Style()
style.theme_use("clam")
style.configure("Custom.Treeview", background="#444", foreground="white")
style.map("Custom.Treeview", background=[("selected", "#555")], foreground=[("selected", "white")])

tree_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
tree_scroll.pack(side="right", fill="y")
tree.configure(yscrollcommand=tree_scroll.set)

delete_button = tk.Button(root, text="Delete", command=lambda: delete_word(dictionary, tree, tree.selection(), root), width=15, bg="#555", fg="white")
delete_button.pack(side="bottom", padx=10, pady=10)

search_button = tk.Button(root, text="Search Word", command=lambda: search_word(dictionary), width=15, bg="#555", fg="white")
search_button.pack(side="bottom", padx=10, pady=10)

test_button = tk.Button(root, text="Test Yourself", command=lambda: test_yourself(dictionary), width=15, bg="#555", fg="white")
test_button.pack(side="bottom", padx=10, pady=10)

dictionary = load_dictionary()
for word, meanings in dictionary.items():
    for meaning in meanings:
        tree.insert("", "end", values=(word, meaning))

root.mainloop()
