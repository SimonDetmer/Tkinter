import tkinter as tk
from tkinter import messagebox
import logbook_database


class LogbookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Logbook")

        self.conn = logbook_database.create_connection("logbook_database.db")
        logbook_database.create_table(self.conn)

        self.entry_text = tk.StringVar()

        # Entry Widget
        self.entry_field = tk.Entry(root, textvariable=self.entry_text)
        self.entry_field.pack(pady=10)

        # Buttons
        self.add_button = tk.Button(root, text="Add Entry", command=self.add_entry)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(root, text="View Entries", command=self.view_entries)
        self.view_button.pack(pady=5)

    def add_entry(self):
        entry = self.entry_text.get()
        if entry:
            logbook_database.insert_entry(self.conn, entry)
            self.entry_text.set("")
            messagebox.showinfo("Success", "Entry added successfully!")
        else:
            messagebox.showwarning("Warning", "Entry cannot be empty!")

    def view_entries(self):
        entries = logbook_database.fetch_entries(self.conn)
        entries_text = "\n".join([f"{row[0]}: {row[1]}" for row in entries])
        messagebox.showinfo("Log Entries", entries_text)


if __name__ == '__main__':
    root = tk.Tk()
    app = LogbookApp(root)
    root.mainloop()
