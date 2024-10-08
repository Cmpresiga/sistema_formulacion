import tkinter as tk
from sqlite3 import ProgrammingError
from style import styles
from components.MainMenu import MainMenu
import Controller


class CreateScreen(tk.Frame):

    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.init_widgets()

    def init_widgets(self):
        tk.Label(
            self,
            text="Ingresa el nombre del producto",
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles. PACK
        )

        self.prod_entry = tk.Entry(
            self,
            justify=tk.CENTER,
            **styles.STYLE
        )

        self.prod_entry.pack(
            **styles.PACK
            )

        self.prod_entry.bind("<Return>", self.add_prod)

        MainMenu(
            self,
            self.manager,
        ).pack(
            **styles.PACK
        )

    def add_prod(self, event):
        prod_name = self.prod_entry.get()
        if prod_name == "":
            tk.messagebox.showinfo(
                title="ERROR",
                message="El nombre del producto no puede estar vacío."
            )
        else:
            try:
                Controller.create_prod(prod_name)
                tk.messagebox.showinfo(
                    title="SUCCESS",
                    message= f"El producto {prod_name} ha sido creado."
                )
            except ProgrammingError:
                tk.messagebox.showinfo(
                    title="ERROR",
                    message="ya existe un producto con este nombre. Prueba otro."
                )