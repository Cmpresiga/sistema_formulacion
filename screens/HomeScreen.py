import tkinter as tk
from style import styles
from components.MainMenu import MainMenu

class HomeScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.init_widgets()

    def init_widgets(self):
        tk.Label(
            self,
            text="Inicio: Menú principal",
            justify=tk.CENTER,
            font = ("Arial", 20)
        ).pack(
            **styles.PACK
        )

        MainMenu(
            self,
            self.manager
        ).pack(
            **styles.PACK
        )