import tkinter as tk
from style import styles
from components.MainMenu import MainMenu

class ReadScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager

    def init_widgets(self, prod, amount,comp_perc):
        try:
            self.helper_frame.pack_forget()
            self.helper_frame.destroy()
        except AttributeError:
            ...
        finally:
            self.helper_frame = tk.Frame(
                self
            )

        self.helper_frame.configure(background=styles.TEXT)
        self.helper_frame.pack(**styles.PACK)

        tk.Label(
            self.helper_frame,
            text = f"Fórmula del: {prod}",
            bg = styles.BACKGROUND,
            fg = "white",
            font = ("Arial", 24),
            anchor="w",
        ).grid(row=0, column=0, columnspan=2, sticky=tk.NSEW, padx = 0, pady = 0)

        tk.Label(
            self.helper_frame,
            text = f"Cantidad de producto: {amount} kg",
            bg = styles.BACKGROUND,
            fg = "white",
            font = ("Arial", 24),
            anchor="w",
        ).grid(row=0, column=2, sticky=tk.NSEW, padx = 0, pady = 0)

        tk.Label(
            self.helper_frame,
            text = "Componentes",
            font = ("Arial", 24),
            anchor="w",
        ).grid(row=1, column=0, sticky=tk.NSEW, padx = 11, pady = 5)

        tk.Label(
            self.helper_frame,
            text = "Porcentajes",
            font = ("Arial", 24),
            anchor="w",
        ).grid(row=1, column=1, sticky=tk.NSEW, padx = 11, pady = 5)

        tk.Label(
            self.helper_frame,
            text = "Cantidades por componente",
            font = ("Arial", 24),
            anchor="w",
        ).grid(row=1, column=2, sticky=tk.NSEW, padx = 11, pady = 5)

        n = 1
        for c_p in comp_perc:
            n += 1
            label_comp = tk.Label(
                self.helper_frame,
                text = c_p[0],
                **styles.STYLE,
                anchor="w",
            )
            label_comp.grid(row=n, column=0, sticky=tk.NSEW, padx = 11, pady = 2)

            label_perc = tk.Label(
                self.helper_frame,
                text = f"{c_p[1] * 100}%",
                **styles.STYLE,
                anchor="e",
            )
            label_perc.grid(row=n, column=1, sticky=tk.NSEW, padx = 11, pady = 2)

            label_amount = tk.Label(
                self.helper_frame,
                text = f"{amount * c_p[1]} kg",
                **styles.STYLE,
                anchor="e",
            )
            label_amount.grid(row=n, column=2, sticky=tk.NSEW, padx = 11, pady = 2)
        
        self.helper_frame.grid_rowconfigure(n+1, weight=1)
        self.helper_frame.grid_columnconfigure(0, weight=1)
        self.helper_frame.grid_columnconfigure(1, weight=1)
        self.helper_frame.grid_columnconfigure(2, weight=1)

        tk.Button(
            self.helper_frame,
            text = "Ver instrucciones",
            command = lambda: self.manager.read_to_inst(),
            **styles.STYLE,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).grid(row= n+1, column=0, columnspan=3, sticky="sew", padx = 11, pady = 11)
        
        MainMenu(
            self.helper_frame,
            self.manager,
        ).grid(row= n+2, column=0, columnspan=3, sticky="sew", padx = 0, pady = 0)