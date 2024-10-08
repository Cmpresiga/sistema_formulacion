import tkinter as tk
import Controller
from screens.HomeScreen import HomeScreen
from screens.CreateScreen import CreateScreen
from screens.UpdateScreen import UpdateScreen
from screens.SelectScreen import SelectScreen
from screens.ReadScreen import ReadScreen
from screens.InstScreen import InstScreen
from screens.DeleteScreen import DeleteScreen


class Manager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Sistema de Formulación")
        self.selected_prod = ""
        self.container = tk.Frame(self)
        self.container.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
        )
        
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)
        
        self.frames = {}

        pantallas = (HomeScreen, CreateScreen, UpdateScreen, SelectScreen, ReadScreen, InstScreen, DeleteScreen)
        for F in pantallas:
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)

        self.show_frame(HomeScreen)


    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


    # Aquí empiezan las transiciones de pantallas

    def home_to_create(self):
        self.show_frame(CreateScreen)

    def home_to_update(self):
        new_options = Controller.get_prod_names()
        self.frames[UpdateScreen].options.update_options(new_options)
        self.show_frame(UpdateScreen)

    def home_to_select(self):
        new_options = Controller.get_prod_names()
        self.frames[SelectScreen].options.update_options(new_options)
        self.show_frame(SelectScreen)

    def select_to_read(self):
        self.selected_prod = self.frames[SelectScreen].options.selected.get()
        self.amount = self.frames[SelectScreen].amount.get()
        if self.selected_prod != "":
            self.comp_perc = Controller.get_prod(self.selected_prod)
            self.frames[ReadScreen].init_widgets(self.selected_prod, self.amount, self.comp_perc)
            self.show_frame(ReadScreen)

    def read_to_inst(self):
        self.selected_prod = self.frames[SelectScreen].options.selected.get()
        self.ints = Controller.get_inst(self.selected_prod)
        self.frames[InstScreen].init_widgets(self.selected_prod, self.ints)
        self.show_frame(InstScreen)

    def home_to_delete(self):
        new_options = Controller.get_prod_names()
        self.frames[DeleteScreen].options.update_options(new_options)
        self.show_frame(DeleteScreen)