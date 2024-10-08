import tkinter as tk
from style import styles
from components.MainMenu import MainMenu
from components.SelectOption import SelectOption
import Controller

class SelectScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.option_list = Controller.get_prod_names()
        self.amount = tk.DoubleVar(self)
        self.init_widgets()


    def init_widgets(self):
        tk.Label(
            self,
            text = "Selecciona el producto a consultar",
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK
        )

        self.options = SelectOption(
            self,
            self.manager,
            self.option_list
        )

        self.options.pack(
            **styles.PACK
        )

        tk.Label(
            self,
            text = "Ingrese la cantidad de producto a fabricar en kg",
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK
        )

        tk.Entry(
            self,
            textvariable=self.amount,
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK
        )

        tk.Button(
            self,
            text = "Ver fórmula",
            command = lambda: self.manager.select_to_read(),
            **styles.STYLE,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )

        MainMenu(
            self,
            self.manager,
        ).pack(
            **styles.PACK
        )