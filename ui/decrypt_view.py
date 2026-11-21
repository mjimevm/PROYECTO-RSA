from core.rsa import desencriptar, generar_claves
import customtkinter as ctk
import customtkinter as ctk
from ui.details_view import detalles_desencriptacion

class DecryptView(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(
            master,
            fg_color="transparent"
        )

        self.grid_columnconfigure(0, weight=1)

        self.create_header()
        self.create_parameters()
        self.create_cipher_input()
        self.create_results()

    def create_header(self):
        ctk.CTkLabel(
            self,
            text="Desencriptar mensaje",
            font=("Poppins", 28, "bold"),
            text_color="#1C1C1C"
        ).grid(
            row=0, column=0,
            sticky="w",
            pady=(0, 8)
        )

        ctk.CTkLabel(
            self,
            text="Recupera el mensaje original utilizando RSA.",
            font=("Poppins", 14),
            text_color="#777777"
        ).grid(
            row=1, column=0,
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
            row=2, column=0,
            sticky="ew",
            pady=(0, 15)
        )

        ctk.CTkLabel(
            frame,
            text="Parámetros RSA",
            font=("Poppins", 18, "bold"),
            text_color="#1C1C1C"
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 15)
        )

        inputs = ctk.CTkFrame(
            frame,
            fg_color="transparent"
        )
        inputs.pack(
            fill="x",
            padx=15,
            pady=(0, 20)
        )

        for i in range(4):
            inputs.grid_columnconfigure(i, weight=1)

        fields = [
            ("Primo p", "p_entry", "367"),
            ("Primo q", "q_entry", "373"),
            ("Exponente e", "e_entry", "17"),
            ("Longitud L", "length_entry", "3")
        ]

        for i, (label, attr, placeholder) in enumerate(fields):
            container = ctk.CTkFrame(
                inputs,
                fg_color="transparent"
            )
            container.grid(
                row=0,
                column=i,
                padx=5,
                sticky="ew"
            )

            ctk.CTkLabel(
                container,
                text=label,
                text_color="#444444"
            ).pack(anchor="w", pady=(0, 6))

            entry = ctk.CTkEntry(
                container,
                placeholder_text=placeholder,
                height=42,
                corner_radius=10,
                fg_color="#FFFFFF",
                border_color="#E5E5E5",
                text_color="#1C1C1C"
            )
            entry.pack(fill="x")

            setattr(self, attr, entry)

    def create_cipher_input(self):
        frame = ctk.CTkFrame(
            self,
            fg_color="#E8E0F3",
            corner_radius=20
        )
        frame.grid(
            row=3, column=0,
            sticky="ew",
            pady=(0, 15)
        )

        ctk.CTkLabel(
            frame,
            text="Mensaje cifrado C",
            font=("Poppins", 18, "bold"),
            text_color="#1C1C1C"
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 12)
        )

        self.cipher_text = ctk.CTkTextbox(
            frame,
            height=95,
            corner_radius=12,
            fg_color="#FFFFFF",
            text_color="#1C1C1C",
            font=("Consolas", 15)
        )
        self.cipher_text.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        self.cipher_text.insert(
            "1.0",
            "026054 123875"
        )

        ctk.CTkButton(
            frame,
            text="Desencriptar mensaje",
            height=45,
            corner_radius=12,
            fg_color="#1C1C1C",
            hover_color="#383838",
            command=self.desencriptar_mensaje
        ).pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

    def create_results(self):
        frame = ctk.CTkFrame(
            self,
            fg_color="#DDF2E3",
            corner_radius=20
        )
        frame.grid(
            row=4, column=0,
            sticky="ew"
        )

        ctk.CTkLabel(
            frame,
            text="Mensaje recuperado",
            font=("Poppins", 18, "bold"),
            text_color="#1C1C1C"
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 12)
        )

        self.result_text = ctk.CTkTextbox(
            frame,
            height=90,
            corner_radius=12,
            fg_color="#FFFFFF",
            text_color="#1C1C1C"
        )
        self.result_text.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )
        self.result_text.configure(state="disabled")

        self.details_label = ctk.CTkLabel(
            frame,
            text="n: --     φ: --     d: --",
            text_color="#444444"
        )
        self.details_label.pack(
            anchor="w",
            padx=20,
            pady=(0, 20)
        )


        # Cuadro para mostrar el procedimiento
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
            pady=(15, 20)
        )

        self.proceso_text.configure(state="disabled")




    def desencriptar_mensaje(self):
        try:
            p = int(self.p_entry.get() or "367")
            q = int(self.q_entry.get() or "373")
            e = int(self.e_entry.get() or "17")

            # Leer la longitud original
            L = int(self.length_entry.get() or "3")

            # Leer todo el contenido, excepto el salto final automatico
            cifrado = self.cipher_text.get("1.0", "end-1c")

            # Mostrar exactamente lo que recibe Python
            print("Cifrado recibido:", repr(cifrado))

            # Desencriptar usando la longitud L
            mensaje = desencriptar(cifrado, L, p, q, e)

            # Mostrar el mensaje recuperado
            self.result_text.configure(state="normal")
            self.result_text.delete("1.0", "end")
            self.result_text.insert("1.0", mensaje)
            self.result_text.configure(state="disabled")

            # Mostrar los valores RSA
            n, d = generar_claves(p, q, e)
            total_coprimos = (p - 1) * (q - 1)

            if L % 2 == 0:
                relleno = "No"
            else:
                relleno = "Si"

            self.details_label.configure(
                text=f"n: {n}     φ: {total_coprimos}     "f"d: {d}     L: {L}     Relleno: {relleno}"
            )


            # Obtener los detalles de la desencriptacion
            detalles = detalles_desencriptacion(
                cifrado, L, p, q, e
            )

            # Mostrar el procedimiento
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


