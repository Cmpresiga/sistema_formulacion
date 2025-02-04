import tkinter as tk
from sqlite3 import ProgrammingError
from style import styles
from components.MainMenu import MainMenu
import Controller


class CreateScreen(tk.Frame):

    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.prod_name = tk.StringVar(self)
        self.comp_name = tk.StringVar(self)
        self.comp_perc = tk.DoubleVar(self)
        self.inst_inst = tk.StringVar(self)
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

        self.input_prod = tk.Entry(
            self,
            textvariable=self.prod_name,
            justify=tk.CENTER,
            **styles.STYLE
        )

        self.input_prod.pack(
            **styles.PACK
            )

        tk.Label(
            self,
            text = "Nombre del componente: ",
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK
        )

        self.input_comp = tk.Entry(
            self,
            textvariable=self.comp_name,
            justify=tk.CENTER,
            **styles.STYLE
        )

        self.input_comp.pack(
            **styles.PACK
        )

        tk.Label(
            self,
            text = "Porcentaje del componente: ",
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK
        )

        input_perc = tk.Entry(
            self,
            textvariable=self.comp_perc,
            justify=tk.CENTER,
            **styles.STYLE
        )
        
        input_perc.pack(
            **styles.PACK
        )

        tk.Button(
            self,
            text = "Añadir componente",
            command = lambda: self.add_formula(),
            **styles.STYLE,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )

        tk.Label(
            self,
            text = "Instrucción: ",
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK
        )

        input_inst = tk.Entry(
            self,
            textvariable=self.inst_inst,
            justify=tk.CENTER,
            **styles.STYLE
        )
        
        input_inst.pack(
            **styles.PACK
        )

        tk.Button(
            self,
            text = "Añadir instrucción",
            command = lambda: self.add_formula(),
            **styles.STYLE,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )

        tk.Button(
            self,
            text = "Crear fórmula",
            command = lambda: self.add_formula(),
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

    def add_formula():
        pass

    def add_prod(self, event):
        prod_name = self.prod_name.get()
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

    def add_comp(self, event):
        _comp_name = self.comp_name.get()
        _comp_perc = self.comp_perc.get() / 100
        _prod_name = self.options.selected.get()
        
        if _comp_name == "" or _comp_perc == "":
            tk.messagebox.showinfo(
                title="ERROR",
                message="El nombre y el porcentaje del componente no pueden estar vacíos."
            )
        else:
            try:
                Controller.create_comp(_comp_name, _comp_perc, _prod_name)
                tk.messagebox.showinfo(
                    title="SUCCESS",
                    message= f"El Componente {_comp_name} ha sido ingresado para el producto {_prod_name}."
                )
            except ProgrammingError:
                tk.messagebox.showinfo(
                    title="ERROR",
                    message=f"El Componente {_comp_name} ya existe para el producto {_prod_name}"
                )
        
        self.comp_name.set("")
        self.comp_perc.set("")

    def add_inst(self,event):
        _inst_inst = self.inst_inst.get()
        _prod_name = self.options.selected.get()

        if _inst_inst == "":
            tk.messagebox.showinfo(
                title="ERROR",
                message="La instrucción no puede estar vacía."
            )
        else:
            Controller.create_inst(_inst_inst, _prod_name)
            tk.messagebox.showinfo(
                title="SUCCESS",
                message= f"La instrucción ha sido ingresada para el producto {_prod_name}."
            )
        
        self.inst_inst.set("")