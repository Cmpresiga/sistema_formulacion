import tkinter as tk
from style import styles
from sqlite3 import ProgrammingError
from components.MainMenu import MainMenu
from components.SelectOption import SelectOption
import Controller

class UpdateScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.option_list = Controller.get_prod_names()
        self.comp_name = tk.StringVar(self)
        self.comp_perc = tk.DoubleVar(self)
        self.inst_inst = tk.StringVar(self)
        self.init_widgets()


    def init_widgets(self):
        tk.Label(
            self,
            text = "Selecciona el producto a editar",
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
            text = "Nombre del componente: ",
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK
        )

        tk.Entry(
            self,
            textvariable=self.comp_name,
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
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

        input_comp = tk.Entry(
            self,
            textvariable=self.comp_perc,
            justify=tk.CENTER,
            **styles.STYLE
        )
        
        input_comp.pack(
            **styles.PACK
        )

        input_comp.bind("<Return>", self.add_comp)

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

        input_inst.bind("<Return>", self.add_inst)

        MainMenu(
            self,
            self.manager,
        ).pack(
            **styles.PACK
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