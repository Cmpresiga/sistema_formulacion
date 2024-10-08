import tkinter as tk
from style import styles


class MainMenu(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background = styles.BACKGROUND)
        self.init_widgets()

    def init_widgets(self):
        tk.Button(
            self,
            text = "Crear una fórmula",
            command = lambda: self.manager.home_to_create(),
            **styles.STYLE,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )

        tk.Button(
            self,
            text = "Consultar una fórmula",
            command = lambda: self.manager.home_to_select(),
            **styles.STYLE,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )

        tk.Button(
            self,
            text = "Editar una fórmula",
            command = lambda: self.manager.home_to_update(),
            **styles.STYLE,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )

        tk.Button(
            self,
            text = "Eliminar una fórmula",
            command = lambda: self.manager.home_to_delete(),
            **styles.STYLE,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )