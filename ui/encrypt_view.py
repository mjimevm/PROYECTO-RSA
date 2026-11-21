
import customtkinter as ctk
from core.rsa import encriptar, generar_claves
from ui.details_view import detalles_encriptacion

class EncryptView(ctk.CTkScrollableFrame):

    def __init__(self, master):
        super().__init__(
            master,
            fg_color="transparent"
        )

        self.grid_columnconfigure(0, weight=1)

        self.create_header()
        self.create_parameters()
        self.create_message()
        self.create_results()

    def create_header(self):
        ctk.CTkLabel(
            self,
            text="Encriptar mensaje",
            font=("Poppins", 28, "bold"),
            text_color="#1C1C1C"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=(5, 8)
        )

        ctk.CTkLabel(
            self,
            text="Convierte un mensaje de texto utilizando RSA.",
            font=("Poppins", 13),
            text_color="#777777"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=(0, 25)
        )

    def create_parameters(self):
        frame = ctk.CTkFrame(
            self,
            fg_color="#F5F5F5",
            corner_radius=20
        )
        frame.grid(
            row=2,
            column=0,
            sticky="ew",
            pady=(0, 16)
        )

        ctk.CTkLabel(
            frame,
            text="Parámetros RSA",
            font=("Poppins", 18, "bold"),
            text_color="#1C1C1C"
        ).pack(
            anchor="w",
            padx=24,
            pady=(22, 15)
        )

        inputs = ctk.CTkFrame(
            frame,
            fg_color="transparent"
        )
        inputs.pack(
            fill="x",
            padx=18,
            pady=(0, 24)
        )

        for i in range(3):
            inputs.grid_columnconfigure(
                i, weight=1, uniform="inputs"
            )

        self.p_entry = self.create_input(
            inputs, "Número primo p", "367", 0
        )
        self.q_entry = self.create_input(
            inputs, "Número primo q", "373", 1
        )
        self.e_entry = self.create_input(
            inputs, "Exponente e", "17", 2
        )

    def create_input(
        self, parent, label, placeholder, column
    ):
        container = ctk.CTkFrame(
            parent,
            fg_color="transparent"
        )
        container.grid(
            row=0,
            column=column,
            padx=6,
            sticky="ew"
        )

        ctk.CTkLabel(
            container,
            text=label,
            font=("Poppins", 13),
            text_color="#444444"
        ).pack(
            anchor="w",
            pady=(0, 7)
        )

        entry = ctk.CTkEntry(
            container,
            placeholder_text=placeholder,
            height=44,
            corner_radius=12,
            fg_color="#FFFFFF",
            border_color="#E5E5E5",
            text_color="#1C1C1C",
            font=("Poppins", 14)
        )
        entry.pack(fill="x")

        return entry

    def create_message(self):
        frame = ctk.CTkFrame(
            self,
            fg_color="#E8E0F3",
            corner_radius=20
        )
        frame.grid(
            row=3,
            column=0,
            sticky="ew",
            pady=(0, 16)
        )

        ctk.CTkLabel(
            frame,
            text="Mensaje original",
            font=("Poppins", 18, "bold"),
            text_color="#1C1C1C"
        ).pack(
            anchor="w",
            padx=24,
            pady=(22, 12)
        )

        self.message_text = ctk.CTkTextbox(
            frame,
            height=110,
            corner_radius=12,
            fg_color="#FFFFFF",
            text_color="#1C1C1C",
            font=("Poppins", 14),
            wrap="word"
        )
        self.message_text.pack(
            fill="x",
            padx=24,
            pady=(0, 16)
        )

        self.encrypt_button = ctk.CTkButton(
            frame,
            text="Encriptar mensaje",
            font=("Poppins", 14, "bold"),
            height=46,
            corner_radius=12,
            fg_color="#1C1C1C",
            hover_color="#383838",
            text_color="#FFFFFF",
            command=self.encriptar_mensaje
        )
        self.encrypt_button.pack(
            fill="x",
            padx=24,
            pady=(0, 24)
        )

    def create_results(self):
        frame = ctk.CTkFrame(
            self,
            fg_color="#DDF2E3",
            corner_radius=20
        )
        frame.grid(
            row=4,
            column=0,
            sticky="ew",
            pady=(0, 16)
        )

        ctk.CTkLabel(
            frame,
            text="Resultado del cifrado",
            font=("Poppins", 18, "bold"),
            text_color="#1C1C1C"
        ).pack(
            anchor="w",
            padx=24,
            pady=(22, 12)
        )

        self.result_text = ctk.CTkTextbox(
            frame,
            height=90,
            corner_radius=12,
            fg_color="#FFFFFF",
            text_color="#1C1C1C",
            font=("Consolas", 15)
        )
        self.result_text.pack(
            fill="x",
            padx=24,
            pady=(0, 15)
        )
        self.result_text.configure(state="disabled")

        self.details_label = ctk.CTkLabel(
            frame,
            text="n: --     φ: --     L: --     Relleno: --",
            font=("Poppins", 13),
            text_color="#444444"
        )
        self.details_label.pack(
            anchor="w",
            padx=24,
            pady=(0, 24)
        )


        # Cuadro para mostrar el procedimiento RSA
        self.proceso_text = ctk.CTkTextbox(
            self,
            height=220,
            corner_radius=12,
            fg_color="#F5F5F5",
            text_color="#1C1C1C",
            font=("Consolas", 14)
        )

        self.proceso_text.grid(
            row=5,
            column=0,
            sticky="ew",
            pady=(0, 20)
        )

        self.proceso_text.configure(state="disabled")





    # Encriptar el mensaje
    def encriptar_mensaje(self):
        try:
            # Obtener los datos ingresados
            p = int(self.p_entry.get() or "367")
            q = int(self.q_entry.get() or "373")
            e = int(self.e_entry.get() or "17")

            mensaje = self.message_text.get("1.0", "end-1c")
            
            # Quitar solamente el salto de linea final del cuadro de texto
            if mensaje.endswith("\n"):
                mensaje = mensaje[:-1]

            # Encriptar el mensaje
            cifrado, L = encriptar(mensaje, p, q, e)

            # Mostrar solamente el mensaje cifrado
            self.result_text.configure(state="normal")
            self.result_text.delete("1.0", "end")
            self.result_text.insert("1.0", cifrado)
            self.result_text.configure(state="disabled")

            # Calcular los valores RSA
            n, d = generar_claves(p, q, e)
            total_coprimos = (p - 1) * (q - 1)

            # Verificar si se agrego relleno
            if L % 2 == 0:
                relleno = "No"
            else:
                relleno = "Si"

            # Mostrar la informacion del proceso
            self.details_label.configure(
                text=f"n: {n}     φ: {total_coprimos}     "f"L: {L}     Relleno: {relleno}     "f"Llave publica: ({e}, {n})"
            )


            # Obtener los detalles de la encriptacion
            detalles = detalles_encriptacion(mensaje, p, q, e)

            # Mostrar los detalles en la interfaz
            self.proceso_text.configure(state="normal")
            self.proceso_text.delete("1.0", "end")
            self.proceso_text.insert("1.0", detalles)
            self.proceso_text.configure(state="disabled")



        except ValueError as error:

            # Limpiar el resultado anterior
            self.result_text.configure(state="normal")
            self.result_text.delete("1.0", "end")
            self.result_text.configure(state="disabled")

            # Limpiar el procedimiento anterior
            self.proceso_text.configure(state="normal")
            self.proceso_text.delete("1.0", "end")
            self.proceso_text.configure(state="disabled")

            # Mostrar el error
            self.details_label.configure(
                text=f"Error: {error}"
            )


