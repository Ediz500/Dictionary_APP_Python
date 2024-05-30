from tkinter import messagebox
from dictionary_data import save_dictionary

def add_word(dictionary, tree, word, meaning):
    if word and meaning:
        if word in dictionary:
            if meaning not in dictionary[word]:
                dictionary[word].append(meaning)
            else:
                messagebox.showerror("Error", "This word and meaning already exist in the dictionary.")
                return False
        else:
            dictionary[word] = [meaning]
        tree.insert("", "end", values=(word, meaning))
        save_dictionary(dictionary)
        return True
    else:
        messagebox.showerror("Error", "Please enter both word and meaning.")
        return False

def delete_word(dictionary, tree, selected_items, root):
    if selected_items:
        for item in selected_items:
            word = tree.item(item, 'values')[0]
            meaning = tree.item(item, 'values')[1]
            if word in dictionary:
                if meaning in dictionary[word]:
                    dictionary[word].remove(meaning)
                    if not dictionary[word]:
                        del dictionary[word]
                    tree.delete(item)
                else:
                    messagebox.showerror("Error", "Selected meaning not found for the word.")
            else:
                messagebox.showerror("Error", "Selected word not found.")
        messagebox.showinfo("Success", "Selected meanings deleted successfully.")
        root.update_idletasks()  # Refresh the window after deleting
        save_dictionary(dictionary)  # Save dictionary to JSON file
    else:
        messagebox.showerror("Error", "Please select at least one word to delete.")



def search_word(dictionary, search_entry, result_label):
    word = search_entry.get()
    if word in dictionary:
        meaning = ", ".join(dictionary[word])
        result_label.config(text=meaning)
    else:
        result_label.config(text="Word not found.")
