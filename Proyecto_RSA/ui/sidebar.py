from pathlib import Path

import customtkinter as ctk
from PIL import Image

ICON_DIR = Path(__file__).resolve().parent.parent / "assets" / "icons"


def load_svg_icon(filename):
    png_filename = Path(filename).with_suffix(".png")
    image = Image.open(ICON_DIR / png_filename)
    return ctk.CTkImage(
        light_image=image,
        dark_image=image,
        size=(22, 22)
    )


icon_dashboard = load_svg_icon("dashboard.svg")
icon_lock = load_svg_icon("lock.svg")
icon_unlock = load_svg_icon("unlock.svg")

class Sidebar(ctk.CTkFrame):

    SIDEBAR_WIDTH = 220

    def __init__(self, master, on_navigate):
        super().__init__(
            master,
            width=self.SIDEBAR_WIDTH,
            corner_radius=22,
            fg_color="#1C1C1C"
        )

        self.on_navigate = on_navigate
        self.active_page = "dashboard"
        self.buttons = {}

        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)

        self.create_header()
        self.create_navigation()

        self.update_buttons()

    def create_header(self):
        self.logo = ctk.CTkLabel(
            self,
            text="RSA",
            font=("Poppins", 20, "bold"),
            text_color="#F8F0D8",
            fg_color="transparent",
            corner_radius=14,
            height=55
        )

        self.logo.grid(
            row=0,
            column=0,
            padx=20,
            pady=(25, 50),
            sticky="ew"
        )

    def create_navigation(self):
        items = [
            ("dashboard", icon_dashboard, "Dashboard"),
            ("encrypt", icon_lock, "Encriptar"),
            ("decrypt", icon_unlock, "Desencriptar")
        ]

        for index, (key, icon, label) in enumerate(items):
            button = ctk.CTkButton(
                self,
                text=label,
                image=icon,
                compound="left",
                height=48,
                corner_radius=12,
                fg_color="transparent",
                hover_color="#353535",
                text_color="#FFFFFF",
                font=("Poppins", 15),
                anchor="w",
                command=lambda page=key: self.navigate(page)
            )

            button.grid(
                row=index + 1,
                column=0,
                sticky="ew",
                padx=16,
                pady=6
            )

            self.buttons[key] = button

    def update_buttons(self):
        for key, button in self.buttons.items():
            button.configure(
                fg_color=(
                    "#353535"
                    if key == self.active_page
                    else "transparent"
                )
            )

    def navigate(self, page):
        self.active_page = page
        self.update_buttons()
        self.on_navigate(page)
