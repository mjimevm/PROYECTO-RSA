
import customtkinter as ctk

from ui.sidebar import Sidebar
from ui.dashboard_view import DashboardView
from ui.encrypt_view import EncryptView
from ui.decrypt_view import DecryptView


class RSAApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.title("RSA Cryptography")
        self.geometry("1280x800")
        self.minsize(1100, 700)

        self.configure(fg_color="#1c1c1c")

        # Configuración del layout
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar fijo
        self.sidebar = Sidebar(
            self,
            on_navigate=self.show_page
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(20, 10),
            pady=20
        )

        # Panel principal
        self.content = ctk.CTkFrame(
            self,
            fg_color="#FFFFFF",
            corner_radius=25
        )

        self.content.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(0, 20),
            pady=20
        )

        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_rowconfigure(0, weight=1)

        # Pantallas
        self.pages = {
            "dashboard": DashboardView(
                self.content,
                on_navigate=self.show_page
            ),
            "encrypt": EncryptView(self.content),
            "decrypt": DecryptView(self.content)
        }

        for page in self.pages.values():
            page.grid(
                row=0,
                column=0,
                sticky="nsew",
                padx=25,
                pady=25
            )

        self.show_page("dashboard")

    def show_page(self, page):
        if page not in self.pages:
            return

        # Ocultar todas las pantallas
        for view in self.pages.values():
            view.grid_remove()

        # Mostrar únicamente la seleccionada
        self.pages[page].grid()

        # Actualizar el botón activo
        self.sidebar.active_page = page
        self.sidebar.update_buttons()
