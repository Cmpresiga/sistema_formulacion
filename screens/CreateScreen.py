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
        self.list_comp = []
        self.list_inst = []
        self.init_widgets()

    def init_widgets(self):

        # try:
        #     self.helper_frame.pack_forget()
        #     self.helper_frame.destroy()
        # except AttributeError:
        #     ...
        # finally:
        #     self.helper_frame = tk.Frame(
        #         self
        #     )
        #     self.helper_frame.configure(background=styles.TEXT)
        #     self.helper_frame.pack(**styles.PACK)

        tk.Label(
            self,
            text="Ingresa el nombre del producto",
            # bg = styles.BACKGROUND,
            # fg = "white",
            font = ("Arial", 24),
            anchor="w",
        ).grid(row=0, column=0, columnspan=5, sticky=tk.NSEW, padx = 11, pady = 5)

        self.input_prod = tk.Entry(
            self,
            textvariable=self.prod_name,
            font = ("Arial", 24),
        ).grid(row=0, column=5, columnspan=3, sticky=tk.NSEW, padx = 11, pady = 5)

        tk.Button(
            self,
            text = "Crear fórmula",
            command = lambda: self.add_formula(),
            font = ("Arial", 24),
            anchor="w",
        ).grid(row=0, column=8, columnspan=2, sticky=tk.NSEW, padx = 11, pady = 5)

        tk.Label(
            self,
            text = "Nombre del componente: ",
            font = styles.FONT,
            anchor="w",
        ).grid(row=1, column=0, columnspan=2, sticky=tk.NSEW, padx = 11, pady = 5)            

        self.input_comp = tk.Entry(
            self,
            textvariable=self.comp_name,
            font = styles.FONT,
        ).grid(row=2, column=0, columnspan=2, sticky=tk.NSEW, padx = 11, pady = 5)

        tk.Label(
            self,
            text = "%",
            font = styles.FONT,
            anchor="w"
        ).grid(row=1, column=2, sticky=tk.NSEW, padx = 11, pady = 5)

        self.input_perc = tk.Entry(
            self,
            textvariable=self.comp_perc,
            font = styles.FONT,
            width=6
        ).grid(row=2, column=2, sticky=tk.NSEW, padx = 11, pady = 5)

        tk.Button(
            self,
            text = "Añadir\ncomponente",
            command = lambda: self.add_formula(),
            font = styles.FONT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).grid(row=1, column=3, rowspan=2, columnspan=2, sticky=tk.NSEW, padx = 11, pady = 5)

        tk.Label(
            self,
            text = "Instrucción: ",
            font = styles.FONT,
            anchor="w",
        ).grid(row=1, column=5, columnspan=3, sticky=tk.NSEW, padx = 11, pady = 5)

        self.input_inst = tk.Entry(
            self,
            textvariable=self.inst_inst,
            font = styles.FONT,
        ).grid(row=2, column=5, columnspan=3, sticky=tk.NSEW, padx = 11, pady = 5)

        tk.Button(
            self,
            text = "Añadir instrucción",
            command = lambda: self.add_formula(),
            font = styles.FONT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).grid(row=1, column=8, rowspan=2, columnspan=2, sticky=tk.NSEW, padx = 11, pady = 5)

        self.helper_frame1 = tk.Frame(self)
        self.helper_frame1.configure(background=styles.TEXT)
        self.helper_frame1.grid(row= 4, column=0, columnspan=5, sticky="nsew", padx = 5, pady = 5)

        tk.Label(
            self.helper_frame1,
            text="Inicio",
            justify=tk.CENTER,
            font = ("Arial", 20)
        ).pack(
            **styles.PACK
        )

        self.helper_frame2 = tk.Frame(self)
        self.helper_frame2.configure(background=styles.TEXT)
        self.helper_frame2.grid(row=4, column=5, columnspan=5, sticky="nsew", padx = 5, pady = 5)

        tk.Label(
            self.helper_frame2,
            text="Inicio: Menú principal",
            justify=tk.CENTER,
            font = ("Arial", 20)
        ).pack(
            **styles.PACK
        )

        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.grid_columnconfigure(2, weight=0)

        MainMenu(
            self,
            self.manager,
        ).grid(row= 5, column=0, columnspan=10, sticky="sew", padx = 0, pady = 0)

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