import tkinter as tk
from style import styles
from components.MainMenu import MainMenu

class InstScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager

    def init_widgets(self, prod, ints):
        try:
            self.helper_frame2.pack_forget()
            self.helper_frame2.destroy()
        except AttributeError:
            ...
        finally:
            self.helper_frame2 = tk.Frame(
                self
            )

        self.helper_frame2.configure(background=styles.TEXT)
        self.helper_frame2.pack(**styles.PACK)

        tk.Label(
            self.helper_frame2,
            text = f"Instrucciones del: {prod}",
            bg = styles.BACKGROUND,
            fg = "white",
            font = ("Arial", 24),
            anchor="w",
        ).pack(
            **styles.PACK2
        )
        n = 0
        for i in ints:
            n += 1 
            tk.Label(
                self.helper_frame2,
                text = f"{n}: {i[0]}",
                **styles.STYLE,
                anchor="w",
            ).pack(
                **styles.PACK
            )

        MainMenu(
            self.helper_frame2,
            self.manager,
        ).pack(
            **styles.PACK2
        )