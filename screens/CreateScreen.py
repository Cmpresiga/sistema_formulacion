import tkinter as tk
from tkinter import messagebox
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
        self.list_perc = []
        self.list_inst = []
        self.init_widgets()
        self.bind("<Configure>", self.on_resize)

    def init_widgets(self):

        tk.Label(
            self,
            text="Ingresa el nombre del producto",
            font = ("Arial", 24),
            anchor="w",
        ).grid(row=0, column=0, columnspan=5, sticky=tk.NSEW, padx = 11, pady = 5)

        tk.Entry(
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

        tk.Entry(
            self,
            textvariable=self.comp_name,
            font = styles.FONT,
        ).grid(row=2, column=0, columnspan=2, sticky=tk.NSEW, padx = 11, pady = 5)

        tk.Label(
            self,
            text = "% p/p",
            font = styles.FONT,
            anchor="w"
        ).grid(row=1, column=2, sticky=tk.NSEW, padx = 11, pady = 5)

        tk.Entry(
            self,
            textvariable=self.comp_perc,
            font = styles.FONT,
            width=6
        ).grid(row=2, column=2, sticky=tk.NSEW, padx = 11, pady = 5)

        tk.Button(
            self,
            text = "Añadir\ncomponente",
            command = lambda: self.add_comp(),
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

        tk.Entry(
            self,
            textvariable=self.inst_inst,
            font = styles.FONT,
        ).grid(row=2, column=5, columnspan=3, sticky=tk.NSEW, padx = 11, pady = 5)

        tk.Button(
            self,
            text = "Añadir\ninstrucción",
            command = lambda: self.add_inst(),
            font = styles.FONT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).grid(row=1, column=8, rowspan=2, columnspan=2, sticky=tk.NSEW, padx = 11, pady = 5)

        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)

        self.helper_frame1 = tk.Frame(self)
        self.helper_frame1.configure(background=styles.TEXT)
        self.helper_frame1.grid(row= 4, column=0, columnspan=5, sticky="nsew", padx = 5, pady = 5)

        tk.Label(
            self.helper_frame1,
            text="Componentes",
            justify=tk.CENTER,
            font = ("Arial", 20)
        ).pack(
            **styles.PACK
        )

        self.helper_frame2 = tk.Frame(self)
        self.helper_frame2.configure(background=styles.TEXT)
        self.helper_frame2.grid(row=4, column=5, columnspan=5, sticky="nsew", padx = 5, pady = 5)
        # self.helper_frame2.grid_columnconfigure(0, weight=1)
        # self.helper_frame2.grid_rowconfigure(0, weight=1)
        
        self.labels = tk.Label(
            self.helper_frame2,
            text="Instrucciones",
            justify=tk.CENTER,
            wraplength= 600,
            font = ("Arial", 20)
        )
        self.labels.pack(
            **styles.PACK
        )

        # self.label_inst..grid(row=0, column=0, sticky="nsew", padx = 5, pady = 5)
        
        MainMenu(
            self,
            self.manager,
        ).grid(row= 5, column=0, columnspan=10, sticky="sew", padx = 0, pady = 0)

    def add_formula(self):
        prod_name = self.prod_name.get()

        if prod_name == "" or self.list_comp == [] or self.list_inst == []:
            tk.messagebox.showinfo(
                title="ERROR",
                message='El nombre del producto, el campo "componentes" o el campo "instrucciones" no pueden estar vacíos.'
            )
        elif sum(self.list_perc) != 100:

            tk.messagebox.showinfo(
                title="ERROR",
                message="la suma de los porcentajes no es 100%. Edite los valores hasta cumplir esta condición."
            )
        else:
            try:
                self.list_perc = [perc / 100 for perc in self.list_perc]
                Controller.create_prod(prod_name, self.list_comp, self.list_perc, self.list_inst)
                tk.messagebox.showinfo(
                    title="SUCCESS",
                    message= f"La fórmula {prod_name} ha sido creada."
                )

                # vaciar el nombre y los campos de componentes e instrucciones , luego de guardar los datos
                self.prod_name.set("")
                self.list_comp = []
                self.list_perc = []
                self.list_inst = []

                # Vacear campo de componentes
                self.helper_frame1.pack_forget()
                self.helper_frame1.destroy()
                self.helper_frame1 = tk.Frame(self)
                self.helper_frame1.configure(background=styles.TEXT)
                self.helper_frame1.grid(row= 4, column=0, columnspan=5, sticky="nsew", padx = 5, pady = 5)

                tk.Label(
                    self.helper_frame1,
                    text="Componentes",
                    justify=tk.CENTER,
                    font = ("Arial", 20)
                ).pack(
                    **styles.PACK
                )

                # Vacear campo de instrucciones
                self.helper_frame2.pack_forget()
                self.helper_frame2.destroy()
                self.helper_frame2 = tk.Frame(self)
                self.helper_frame2.configure(background=styles.TEXT)
                self.helper_frame2.grid(row=4, column=5, columnspan=5, sticky="nsew", padx = 5, pady = 5)
                
                self.labels = tk.Label(
                    self.helper_frame2,
                    text="Instrucciones",
                    justify=tk.CENTER,
                    wraplength= 600,
                    font = ("Arial", 20)
                )
                self.labels.pack(
                    **styles.PACK
                )

            except ProgrammingError:
                tk.messagebox.showinfo(
                    title="ERROR",
                    message="Ya existe un producto con este nombre. Prueba otro."
                )

    def add_comp(self):
        _comp_name = self.comp_name.get()
        _comp_perc = self.comp_perc.get()
        
        if _comp_name == "" or _comp_perc == 0.0 or _comp_perc == "":
            tk.messagebox.showinfo(
                title="ERROR",
                message="El nombre y el porcentaje del componente no pueden estar vacíos o ser = 0.0."
            )
        elif _comp_name.lower() in [v.lower() for v in self.list_comp]:
            tk.messagebox.showinfo(
                title="ERROR",
                message=f"El Componente {_comp_name} ya existe."
            )
        else:
            self.list_comp.append(_comp_name)
            self.list_perc.append(_comp_perc)
            self.gen_frame_comp()
            self.comp_name.set("")
            self.comp_perc.set(0.0)
            
    def upd_comp(self, x):
        self.helper_frame1.pack_forget()
        self.helper_frame1.destroy()
        self.helper_frame1 = tk.Frame(self)
        self.helper_frame1.configure(background=styles.TEXT)
        self.helper_frame1.grid(row=4, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)

        n=0
        for comp in self.list_comp:
            if comp == self.list_comp[x]:
                self.comp_input = tk.StringVar(value=f"{comp}")
                tk.Entry(
                    self.helper_frame1,
                    textvariable=self.comp_input,
                    font = styles.FONT,
                    width=20
                ).grid(row=n, column=0, columnspan=2, sticky=tk.NSEW, padx = 5, pady = 5)

                self.perc_input = tk.DoubleVar(value=f"{self.list_perc[x]}")
                tk.Entry(
                    self.helper_frame1,
                    textvariable= self.perc_input,
                    font = styles.FONT,
                    width=6
                ).grid(row=n, column=2, sticky=tk.NSEW, padx = 16, pady = 5)
                
                tk.Button(
                    self.helper_frame1,
                    text = "Confir",
                    command = lambda x=n: self.confir_upd(x),
                    font = ("Arial", 12),
                    activebackground=styles.BACKGROUND,
                    activeforeground=styles.TEXT
                ).grid(row=n, column=3, sticky=tk.NSEW, padx = 5, pady = 5)

                tk.Button(
                    self.helper_frame1,
                    text = "Cancel",
                    command = lambda: self.cancel_upd(),
                    font = ("Arial", 12),
                    activebackground=styles.BACKGROUND,
                    activeforeground=styles.TEXT
                ).grid(row=n, column=4, sticky=tk.NSEW, padx = 5, pady = 5)
            else:
                tk.Label(
                    self.helper_frame1,
                    text = f"{comp}",
                    font = styles.FONT,
                    anchor="w",
                    width=20
                ).grid(row=n, column=0, columnspan=2, sticky=tk.NSEW, padx = 5, pady = 5)

                tk.Label(
                    self.helper_frame1,
                    text = f"{self.list_perc[n]}",
                    font = styles.FONT,
                    anchor="e",
                    width=6
                ).grid(row=n, column=2, sticky=tk.NSEW, padx = 16, pady = 5)

                tk.Button(
                    self.helper_frame1,
                    text = "Editar",
                    command = lambda x=n: self.upd_comp(x),
                    font = ("Arial", 12),
                    activebackground=styles.BACKGROUND,
                    activeforeground=styles.TEXT
                ).grid(row=n, column=3, sticky=tk.NSEW, padx = 5, pady = 5)

                tk.Button(
                    self.helper_frame1,
                    text = "Borrar",
                    command = lambda x=n: self.del_comp(x),
                    font = ("Arial", 12),
                    activebackground=styles.BACKGROUND,
                    activeforeground=styles.TEXT
                ).grid(row=n, column=4, sticky=tk.NSEW, padx = 5, pady = 5)
        
            n += 1

    def confir_upd(self, x):
        _comp_input = self.comp_input.get()
        _perc_input = self.perc_input.get()

        if _comp_input == "" or _perc_input == 0.0 or _perc_input == "":
            tk.messagebox.showinfo(
                title="ERROR",
                message="El nombre y el porcentaje del componente no pueden estar vacíos o ser = 0.0."
            )
        elif _comp_input.lower() in [v.lower() for v in self.list_comp] and _comp_input.lower() != self.list_comp[x].lower():
            tk.messagebox.showinfo(
            title="ERROR",
            message=f"El Componente {_comp_input} ya existe."
            )
        else:
            self.list_comp[x] = _comp_input
            self.list_perc[x] = _perc_input
            self.gen_frame_comp()

    def cancel_upd(self):
        self.gen_frame_comp()

    def del_comp(self, x):
        del self.list_comp[x]
        del self.list_perc[x]
        if self.list_comp != []:
            self.gen_frame_comp()
        else:
            self.helper_frame1.pack_forget()
            self.helper_frame1.destroy()
            self.helper_frame1 = tk.Frame(self)
            self.helper_frame1.configure(background=styles.TEXT)
            self.helper_frame1.grid(row= 4, column=0, columnspan=5, sticky="nsew", padx = 5, pady = 5)

            tk.Label(
                self.helper_frame1,
                text="Componentes",
                justify=tk.CENTER,
                font = ("Arial", 20)
            ).pack(
                **styles.PACK
            )

    def gen_frame_comp(self):
        self.helper_frame1.pack_forget()
        self.helper_frame1.destroy()
        self.helper_frame1 = tk.Frame(self)
        self.helper_frame1.configure(background=styles.TEXT)
        self.helper_frame1.grid(row= 4, column=0, columnspan=5, sticky="nsew", padx = 5, pady = 5)

        n=0
        for comp in self.list_comp:
            tk.Label(
                self.helper_frame1,
                text = f"{comp}",
                font = styles.FONT,
                anchor="w",
                width=20
            ).grid(row=n, column=0, columnspan=2, sticky=tk.NSEW, padx = 5, pady = 5)

            tk.Label(
                self.helper_frame1,
                text = f"{self.list_perc[n]}",
                font = styles.FONT,
                anchor="e",
                width=6
            ).grid(row=n, column=2, sticky=tk.NSEW, padx = 16, pady = 5)

            tk.Button(
                self.helper_frame1,
                text = "Editar",
                command = lambda x=n: self.upd_comp(x),
                font = ("Arial", 12),
                activebackground=styles.BACKGROUND,
                activeforeground=styles.TEXT
            ).grid(row=n, column=3, sticky=tk.NSEW, padx = 5, pady = 5)

            tk.Button(
                self.helper_frame1,
                text = "Borrar",
                command = lambda x=n: self.del_comp(x),
                font = ("Arial", 12),
                activebackground=styles.BACKGROUND,
                activeforeground=styles.TEXT
            ).grid(row=n, column=4, sticky=tk.NSEW, padx = 5, pady = 5)

            n += 1
        
    def add_inst(self):

        _inst_inst = self.inst_inst.get()

        if _inst_inst == "":
            tk.messagebox.showinfo(
                title="ERROR",
                message="La instrucción no puede estar vacía."
            )
        else:
            self.list_inst.append(_inst_inst)
            self.gen_frame_inst()
            self.inst_inst.set("")
        
    def gen_frame_inst(self):
        self.helper_frame2.pack_forget()
        self.helper_frame2.destroy()
        self.helper_frame2 = tk.Frame(self)
        self.helper_frame2.configure(background=styles.TEXT)
        self.helper_frame2.grid(row= 4, column=5, columnspan=5, sticky="nsew", padx = 5, pady = 5)

        self.labels = []
        for n, inst in enumerate(self.list_inst):

            self.helper_frame2.grid_columnconfigure(n, weight=1)

            label = tk.Label(
                self.helper_frame2,
                text = f"{n+1}: {inst}",
                wraplength= 480,
                justify="left",
                font = styles.FONT,
                anchor="w"
            )
            label.grid(row=n, column=0, columnspan=3, sticky=tk.NSEW, padx = 5, pady = 5)

            tk.Button(
                self.helper_frame2,
                text = "Editar",
                command = lambda x=n: self.upd_inst(x),
                font = ("Arial", 12),
                activebackground=styles.BACKGROUND,
                activeforeground=styles.TEXT
            ).grid(row=n, column=3, sticky=tk.NSEW, padx = 5, pady = 5)

            tk.Button(
                self.helper_frame2,
                text = "Borrar",
                command = lambda x=n: self.del_inst(x),
                font = ("Arial", 12),
                activebackground=styles.BACKGROUND,
                activeforeground=styles.TEXT
            ).grid(row=n, column=4, sticky=tk.NSEW, padx = 5, pady = 5)

            self.labels.append(label)
        
        self.after(50, self.update_labels_size)

    def on_resize(self, event):
        # print(event.width, event.height)
        self.after(50, self.update_labels_size)

    def update_labels_size(self):

        if type(self.labels) == list:
            
            for label in self.labels:
                nuevo_ancho = label.winfo_width()
                label.config(wraplength=nuevo_ancho)

        else:
            nuevo_ancho = self.labels.winfo_width()
            self.labels.config(wraplength=nuevo_ancho)
            # print(f"Nuevo ancho actualizado: {nuevo_ancho}")

    def upd_inst(self, x):
        self.helper_frame2.pack_forget()
        self.helper_frame2.destroy()
        self.helper_frame2 = tk.Frame(self)
        self.helper_frame2.configure(background=styles.TEXT)
        self.helper_frame2.grid(row=4, column=5, columnspan=5, sticky="nsew", padx = 5, pady = 5)

        for n, inst in enumerate(self.list_inst):

            self.helper_frame2.grid_columnconfigure(n, weight=1)

            if inst == self.list_inst[x]:
                self.inst_input = tk.StringVar(value=f"{inst}")

                # Tarea: hacer que el entry se extienda igual de la label, al redimensionar la pantalla

                tk.Entry(
                    self.helper_frame2,
                    textvariable=self.inst_input,
                    font = styles.FONT,
                    width=20
                ).grid(row=n, column=0, columnspan=3, sticky=tk.NSEW, padx = 5, pady = 5)

                tk.Button(
                    self.helper_frame2,
                    text = "Confir",
                    command = lambda x=n: self.confir_upd_inst(x),
                    font = ("Arial", 12),
                    activebackground=styles.BACKGROUND,
                    activeforeground=styles.TEXT
                ).grid(row=n, column=3, sticky=tk.NSEW, padx = 5, pady = 5)

                tk.Button(
                    self.helper_frame2,
                    text = "Cancel",
                    command = lambda: self.cancel_upd_inst(),
                    font = ("Arial", 12),
                    activebackground=styles.BACKGROUND,
                    activeforeground=styles.TEXT
                ).grid(row=n, column=4, sticky=tk.NSEW, padx = 5, pady = 5)
            else:
                tk.Label(
                    self.helper_frame2,
                    text = f"{n+1}: {inst}",
                    font = styles.FONT,
                    anchor="w",
                    width=20
                ).grid(row=n, column=0, columnspan=3, sticky=tk.NSEW, padx = 5, pady = 5)

                tk.Button(
                    self.helper_frame2,
                    text = "Editar",
                    command = lambda x=n: self.upd_inst(x),
                    font = ("Arial", 12),
                    activebackground=styles.BACKGROUND,
                    activeforeground=styles.TEXT
                ).grid(row=n, column=3, sticky=tk.NSEW, padx = 5, pady = 5)

                tk.Button(
                    self.helper_frame2,
                    text = "Borrar",
                    command = lambda x=n: self.del_inst(x),
                    font = ("Arial", 12),
                    activebackground=styles.BACKGROUND,
                    activeforeground=styles.TEXT
                ).grid(row=n, column=4, sticky=tk.NSEW, padx = 5, pady = 5)

    def confir_upd_inst(self, x):
        _inst_input = self.inst_input.get()

        if _inst_input == "":
            tk.messagebox.showinfo(
                title="ERROR",
                message="La instrucción no puede estar vacía"
            )
        # elif _inst_input.lower() in [v.lower() for v in self.list_inst] and _inst_input.lower() != self.list_inst[x].lower():
        #     tk.messagebox.showinfo(
        #     title="ERROR",
        #     message=f"La instrucción {_inst_input} ya existe."
        #     )
        else:
            self.list_inst[x] = _inst_input
            self.gen_frame_inst()

    def cancel_upd_inst(self):
        self.gen_frame_inst()

    def del_inst(self, x):
        del self.list_inst[x]
        if self.list_inst != []:
            self.gen_frame_inst()
        else:
            self.helper_frame2.pack_forget()
            self.helper_frame2.destroy()
            self.helper_frame2 = tk.Frame(self)
            self.helper_frame2.configure(background=styles.TEXT)
            self.helper_frame2.grid(row=4, column=5, columnspan=5, sticky="nsew", padx = 5, pady = 5)
            
            self.labels = tk.Label(
                self.helper_frame2,
                text="Instrucciones",
                justify=tk.CENTER,
                wraplength= 600,
                font = ("Arial", 20)
            )
            self.labels.pack(
                **styles.PACK
            )
