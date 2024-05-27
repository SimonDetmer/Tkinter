import tkinter as tk
from tkinter import messagebox
import logbook_database


class LogbookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Logbuch")

        # Datenbankverbindung und Tabelleninitialisierung
        self.conn = logbook_database.create_connection("logbook_database.db")
        logbook_database.create_table(self.conn)

        # Entry Label und Entry Widget
        self.entry_text = tk.StringVar()
        self.entry_label = tk.Label(root, text="Neuer Eintrag:")
        self.entry_label.pack(pady=(10, 0))
        self.entry_field = tk.Entry(root, textvariable=self.entry_text)
        self.entry_field.pack(fill=tk.BOTH, pady=(0, 10))

        # Buttons
        self.add_button = tk.Button(root, text="Eintrag hinzufügen", command=self.add_entry, fg='white', bg='blue',)
        self.add_button.pack(pady=5)

        # Logbook-Label
        self.log_label = tk.Label(root, text="Alle Einträge:")
        self.log_label.pack(pady=(30, 0))

        # ShowLogbook
        self.log_frame = tk.Frame(root)
        self.log_frame.pack(fill=tk.BOTH, expand=True)

        self.log_text = tk.Text(self.log_frame, wrap=tk.WORD, width=50, height=10)
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Erweiterung der des Logbuchfensters um einen Scrollbalken
        self.log_scrollbar = tk.Scrollbar(self.log_frame, orient=tk.VERTICAL, command=self.log_text.yview)
        self.log_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.log_text.config(yscrollcommand=self.log_scrollbar.set)

        self.load_entries()

    # Methode zum Laden der Einträge
    def load_entries(self):
        self.log_text.delete(1.0, tk.END)
        entries = logbook_database.fetch_entries(self.conn)
        for entry in entries:
            self.log_text.insert(tk.END, f"{entry[0]}: {entry[1]}\n\n")


    # Methode zum Hinzufügen neuer Einträge
    def add_entry(self):
        entry = self.entry_text.get()
        if entry:
            logbook_database.insert_entry(self.conn, entry)
            self.entry_text.set("")
            self.load_entries()
            messagebox.showinfo("Erfolg", "Eintrag wurde hinzugefügt")
        else:
            messagebox.showwarning("Fehler", "Das Eingabefeld ist leer")

# Ausführung des Programms
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('400x350')
    app = LogbookApp(root)
    root.mainloop()

