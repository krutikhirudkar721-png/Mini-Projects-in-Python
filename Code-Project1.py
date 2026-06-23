import json
import datetime
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

FILE = "notes.json"


# Load notes
def load_notes():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

# Save notes
def save_notes(notes):
    with open(FILE, "w") as f:
        json.dump(notes, f, indent=4)

class NotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Notes GUI")
        self.root.geometry("500x500")

        self.notes = load_notes()
        self.listbox = tk.Listbox(root, width=60, height=20)
        self.listbox.pack(pady=10)

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Add", width=10, command=self.add_note).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Delete", width=10, command=self.delete_note).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Search", width=10, command=self.search_notes).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Refresh", width=10, command=self.refresh_list).grid(row=0, column=3, padx=5)

        self.refresh_list()

    def refresh_list(self):
        self.notes = load_notes()
        self.listbox.delete(0, tk.END)
        for note in self.notes:
            display = f"{note['text']} | {note['tag']} | {note['time']}"
            self.listbox.insert(tk.END, display)

    def add_note(self):
        text = simpledialog.askstring("Input", "Enter note:")
        if not text:
            return

        tag = simpledialog.askstring("Input", "Enter tag:")
        if not tag:
            tag = "general"

        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.notes.append({"text": text, "tag": tag, "time": time})
        save_notes(self.notes)
        self.refresh_list()
        messagebox.showinfo("Success", "Note added!")

    def delete_note(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Select a note first")
            return

        index = selected[0]
        self.notes.pop(index)
        save_notes(self.notes)
        self.refresh_list()
        messagebox.showinfo("Deleted", "Note deleted!")

    def search_notes(self):
        keyword = simpledialog.askstring("Search", "Enter keyword:")
        if not keyword:
            return

        results = []
        for note in self.notes:
            if keyword.lower() in note["text"].lower():
                results.append(note)

        if not results:
            messagebox.showinfo("Search", "No matching notes")
            return

        self.listbox.delete(0, tk.END)
        for note in results:
            display = f"{note['text']} | {note['tag']} | {note['time']}"
            self.listbox.insert(tk.END, display)

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = NotesApp(root)
    root.mainloop()
