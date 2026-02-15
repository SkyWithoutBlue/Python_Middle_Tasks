#Main.py
from MainWindow import MainWindow
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()

#MainWindow.py
import tkinter as tk
from tkinter import scrolledtext, filedialog
from AboutWindow import About

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Блокнот")
        self.geometry("800x600")
        self.edit_text = scrolledtext.ScrolledText(width=96, height=37)
        self._create_menu()
        self.edit_text.pack()
    def _open_file(self):
        self._filepath = filedialog.askopenfilename()
        if self._filepath != "":
            with open(self._filepath, "r") as file:
                text = file.read()
                self.title(f"Блокнот {file.name}")
                self.edit_text.delete("1.0", tk.END)
                self.edit_text.insert("1.0", text)

    def _save_file_as(self):
        self._filepath = filedialog.asksaveasfilename()
        self._save_file()
    def _save_file(self):
        if self._filepath != "":
            text = self.edit_text.get("1.0", tk.END)
            with open(self._filepath, "w") as file:
                file.write(text)
        else:
            self._save_file_as()
    def _create_menu(self):
        self._menu = tk.Menu(self,tearoff=0)
        self._menu.add_command(label="Открыть файл", command=self._open_file)
        self._menu.add_command(label="Сохранить файл как", command=self._save_file_as)
        self._menu.add_command(label="Сохранить файл", command=self._save_file)
        self._menu.add_command(label="О программе", command=self._open_about)
        self.config(menu=self._menu)
    def _open_about(self):
        about = About(self)
        about.grab_set()

  #AboutWindow.py
import tkinter as tk
class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text="Версия: 1.0")
        self.button = tk.Button(self, text="Закрыть", command=self.destroy)

        self.label.pack(padx=20, pady=20)
        self.button.pack(pady=5, ipadx=2, ipady=2)
