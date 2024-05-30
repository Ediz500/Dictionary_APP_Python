import tkinter as tk
from tkinter import messagebox
import random


def test_yourself(dictionary):
    if not dictionary:
        messagebox.showwarning("Warning", "The dictionary is empty. Please add words before testing yourself.")
        return

    def check_answer():
        nonlocal current_word_index, current_meaning
        user_answer = answer_entry.get().strip()
        answer = "".join(current_meaning)

        if user_answer.lower() == answer.lower():
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showerror("Result", f"Incorrect! The correct meaning is: {current_meaning}")

        current_word_index += 1
        if current_word_index < len(words):
            ask_question()
        else:
            messagebox.showinfo("Test Completed", "You have completed the test.")
            

    def ask_question():
        nonlocal current_word, current_meaning
        current_word = words[current_word_index]
        current_meaning = dictionary[current_word]
        question_label.config(text=f"What is the meaning of '{current_word}'?")
        answer_entry.delete(0, tk.END)

    test_window = tk.Toplevel()
    test_window.title("Test Yourself")
    test_window.configure(bg="#333")
    test_frame = tk.Frame(test_window, bg="#333")
    test_frame.pack(padx=20, pady=20)
    question_label = tk.Label(test_frame, text="", bg="#333", fg="white")
    question_label.grid(row=0, column=0, padx=5, pady=5)
    answer_entry = tk.Entry(test_frame, bg="#333", fg="white")
    answer_entry.grid(row=1, column=0, padx=5, pady=5)
    submit_button = tk.Button(test_frame, text="Submit", command=check_answer, bg="#555", fg="white")
    submit_button.grid(row=2, column=0, padx=5, pady=5)

    words = list(dictionary.keys())
    random.shuffle(words)
    current_word_index = 0
    current_word = ""
    current_meaning = ""
    ask_question()
