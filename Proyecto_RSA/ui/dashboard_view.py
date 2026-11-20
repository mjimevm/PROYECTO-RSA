
import customtkinter as ctk

from ui.sidebar import icon_dashboard


class DashboardView(ctk.CTkFrame):

    OUTER_PADDING = 16
    CARD_GAP = 8
    CARD_PADDING = 24
    SECTION_GAP = 25

    def __init__(self, master, on_navigate):
        super().__init__(
            master,
            fg_color="transparent",
            corner_radius=0
        )

        self.on_navigate = on_navigate
        self.grid_columnconfigure(0, weight=1)

        self.create_header()
        self.create_cards()
        self.create_actions()

    def create_header(self):
        ctk.CTkLabel(
            self,
            text="Vista General",
            font=("Poppins", 30, "bold"),
            text_color="#1C1C1C",
            anchor="w"
        ).grid(
            row=0,
            column=0,
            sticky="ew",
            padx=self.OUTER_PADDING,
            pady=(0, 8)
        )

        ctk.CTkLabel(
            self,
            text="Bienvenido al sistema de criptografía RSA",
            font=("Poppins", 14),
            text_color="#777777"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=self.OUTER_PADDING,
            pady=(0, self.SECTION_GAP)
        )

    def create_cards(self):
        cards = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        cards.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=self.OUTER_PADDING - self.CARD_GAP
        )

        for i in range(3):
            cards.grid_columnconfigure(
                i,
                weight=1,
                uniform="cards"
            )

        self.create_card(
            cards, 0,
            "Encriptación",
            "RSA",
            "#E3F1FF"
        )

        self.create_card(
            cards, 1,
            "Llave pública",
            "(e, n)",
            "#E8E0F3"
        )

        self.create_card(
            cards, 2,
            "Llave privada",
            "(d, n)",
            "#DDF2E3"
        )


    def create_card(self, parent, column, title, value, color):
        card = ctk.CTkFrame(
            parent,
            fg_color=color,
            corner_radius=20
        )

        card.grid(
            row=0,
            column=column,
            sticky="nsew",
            padx=8,
            pady=4
        )

        card.grid_columnconfigure(0, weight=1)

        title_label = ctk.CTkLabel(
            card,
            text=title,
            font=("Poppins", 14),
            text_color="#444444",
            anchor="w"
        )
        title_label.pack(
            fill="x",
            padx=self.CARD_PADDING,
            pady=(25, 5)
        )

        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=("Poppins", 27, "bold"),
            text_color="#1C1C1C",
            anchor="w"
        )
        value_label.pack(
            fill="x",
            padx=self.CARD_PADDING,
            pady=(0, 30)
        )


    def create_actions(self):
        ctk.CTkLabel(
            self,
            text="Operaciones",
            font=("Poppins", 20, "bold"),
            text_color="#1C1C1C"
        ).grid(
            row=3,
            column=0,
            sticky="w",
            padx=self.OUTER_PADDING,
            pady=(self.SECTION_GAP, 16)
        )

        actions = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        actions.grid(
            row=4,
            column=0,
            sticky="ew",
            padx=self.OUTER_PADDING - self.CARD_GAP
        )

        for i in range(2):
            actions.grid_columnconfigure(
                i,
                weight=1,
                uniform="actions"
            )

        self.create_action(
            actions,
            0,
            "Encriptar mensaje",
            "Convertir texto a bloques cifrados",
            "encrypt"
        )

        self.create_action(
            actions,
            1,
            "Desencriptar mensaje",
            "Recuperar el texto original",
            "decrypt"
        )

    def create_action(
        self, parent, column, title, description, page
    ):
        card = ctk.CTkFrame(
            parent,
            fg_color="#F5F5F5",
            corner_radius=20
        )

        card.grid(
            row=0,
            column=column,
            sticky="nsew",
            padx=self.CARD_GAP,
            pady=4
        )

        ctk.CTkLabel(
            card,
            text=title,
            font=("Poppins", 17, "bold"),
            text_color="#1C1C1C"
        ).pack(
            anchor="w",
            padx=self.CARD_PADDING,
            pady=(24, 6)
        )

        ctk.CTkLabel(
            card,
            text=description,
            font=("Poppins", 13),
            text_color="#777777",
            wraplength=280,
            justify="left"
        ).pack(
            anchor="w",
            padx=self.CARD_PADDING
        )

        ctk.CTkButton(
            card,
            text="Abrir",
            font=("Poppins", 13, "bold"),
            fg_color="#1C1C1C",
            hover_color="#383838",
            corner_radius=12,
            height=40,
            width=110,
            command=lambda: self.on_navigate(page)
        ).pack(
            anchor="w",
            padx=self.CARD_PADDING,
            pady=(22, 24)
        )
