import tkinter as tk
from style import styles
from components.MainMenu import MainMenu
from components.SelectOption import SelectOption
import Controller

class DeleteScreen(tk.Frame):

    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.option_list = Controller.get_prod_names()
        self.init_widgets()


    def init_widgets(self):
        tk.Label(
            self,
            text = "Selecciona el producto a eliminar",
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

        tk.Button(
            self,
            text = "Eliminar fórmula",
            command = lambda: self.delete_prod(),
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
    
    def delete_prod(self):
        prod = self.options.selected.get()
        tk.messagebox.showinfo(
            title="WARNING",
            message=f"¿Deseas borrar la fórmula del producto {prod}?"
        )
        Controller.delete_prod(prod)
        tk.messagebox.showinfo(
            title="SUCCESS",
            message=f"La fórmula del producto {prod} ha sido eliminada"
        )
        new_options = Controller.get_prod_names()
        self.options.update_options(new_options)