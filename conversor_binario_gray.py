import tkinter as tk
from tkinter import messagebox

# =====================================================
# FUNCIONES DE CONVERSIÓN Y MENSAJES
# =====================================================


def mostrar_mensaje(texto, tipo="ok"):
    """
    Muestra un mensaje en la etiqueta inferior con un color según el tipo:
      - Verde: correcto
      - Rojo: error
    """
    if tipo == "ok":
        label_mensaje.config(text=texto, fg="#00ff9c")
    else:
        label_mensaje.config(text=texto, fg="#ff6464")


# === Conversión Decimal a Binario (4 bits) ===
def decimal_a_binario(event=None):
    """
    Convierte un número decimal entre 0 y 15 en binario de 4 bits.
    Se limpia el campo al finalizar.
    """
    entrada = entry_decimal.get().strip()
    # if not entrada.isdigit():
    #     mostrar_mensaje("❌ Ingresa solo números enteros.", "error")
    #     entry_decimal.delete(0, tk.END)
    #     return

    decimal = int(entrada)
    if 0 <= decimal <= 15:
        binario = format(decimal, "04b")
        mostrar_mensaje(f"✅ {decimal} en binario (4 bits) = {binario}", "ok")
    else:
        mostrar_mensaje("⚠️ Ingresa un número entre 0 y 15.", "error")
        entry_decimal.delete(0, tk.END)


# === Suma de dos binarios de 2 bits ===
def sumar_binarios(event=None):
    """
    Suma dos binarios de 2 bits e imprime el resultado en binario y decimal.
    Si los valores no son válidos, se limpian los campos y se muestra error.
    """
    b1 = entry_bin1.get().strip()
    b2 = entry_bin2.get().strip()

    # if not (len(b1) == len(b2) == 2 and all(c in "01" for c in b1 + b2)):
    #     mostrar_mensaje(
    #         "❌ Ingresa dos binarios válidos de 2 bits (solo 0 o 1).", "error"
    #     )
    #     entry_bin1.delete(0, tk.END)
    #     entry_bin2.delete(0, tk.END)
    #     return

    suma = int(b1, 2) + int(b2, 2)
    resultado_bin = format(suma, "03b")
    mostrar_mensaje(f"✅ {b1} + {b2} = {resultado_bin} (decimal {suma})", "ok")
    entry_bin1.delete(0, tk.END)
    entry_bin2.delete(0, tk.END)


# === Conversión Binario a Código Gray (5 bits) ===
def binario_a_gray(event=None):
    """
    Convierte un número binario de 5 bits a su código Gray equivalente.
    Si hay caracteres inválidos o longitud incorrecta, se muestra error.
    """
    b = entry_gray.get().strip()
    if len(b) != 5 or any(c not in "01" for c in b):
        mostrar_mensaje("❌ Ingresa un número binario de 5 bits (ej: 10110).", "error")
        entry_gray.delete(0, tk.END)
        return

    gray = b[0]
    for i in range(1, len(b)):
        gray += str(int(b[i - 1]) ^ int(b[i]))  # XOR entre bits consecutivos

    mostrar_mensaje(f"✅ Código Gray de {b} = {gray}", "ok")
    entry_gray.delete(0, tk.END)


# =====================================================
# FUNCIONES DE VALIDACIÓN DE ENTRADA
# =====================================================


def limitar_entrada_decimal(event):
    """
    Permite solo dígitos y limita a 2 caracteres (máximo 15 en decimal).
    """
    valor = entry_decimal.get()
    if not valor.isdigit():
        entry_decimal.delete(0, tk.END)
        mostrar_mensaje("❌ Ingresa solo números enteros.", "error")
    elif len(valor) > 2:
        entry_decimal.delete(2, tk.END)
        mostrar_mensaje("⚠️ Ingresa un número de dos digitos entre 0 y 15.", "error")


def limitar_entrada_bin(entry, max_bits):
    """
    Permite solo caracteres '0' o '1' y limita la cantidad máxima de bits.
    """
    valor = entry.get()
    if any(c not in "01" for c in valor):
        mostrar_mensaje(
            "❌ Solo se permite numeros binarios válidos de 2 bits (solo 0 o 1).",
            "error",
        )
        entry.delete(0, tk.END)
    elif len(valor) > max_bits:
        mostrar_mensaje(
            "❌ Haz sobrepasado el número de bits solicitado",
            "error",
        )
        entry.delete(max_bits, tk.END)


# =====================================================
# INTERFAZ GRÁFICA PRINCIPAL
# =====================================================

ventana = tk.Tk()
ventana.title("🧮 Conversor Binario y Código Gray")
ventana.geometry("480x520")
ventana.config(bg="#1c1c2e")
ventana.resizable(True, True)  # Se puede redimensionar la ventana

# --- Título Principal ---
tk.Label(
    ventana,
    text="Conversor Decimal ↔ Binario + Código Gray",
    font=("Arial", 15, "bold"),
    fg="#ffffff",
    bg="#1c1c2e",
).pack(pady=15)

# --- Mensaje informativo (inferior) ---
label_mensaje = tk.Label(
    ventana,
    text="Bienvenido 👋 Ingresa tus datos abajo.",
    font=("Arial", 10),
    bg="#1c1c2e",
    fg="#cccccc",
)
label_mensaje.pack(pady=5)

# =====================================================
# 1️⃣ Decimal a Binario (4 bits)
# =====================================================
frame1 = tk.LabelFrame(
    ventana,
    text="1️⃣ Decimal a Binario (4 bits)",
    bg="#2b2b40",
    fg="white",
    font=("Arial", 11, "bold"),
)
frame1.pack(padx=20, pady=10, fill="x")

tk.Label(frame1, text="Número decimal (0–15):", bg="#2b2b40", fg="white").pack()
entry_decimal = tk.Entry(frame1, justify="center", font=("Arial", 12))
entry_decimal.pack(pady=5)
entry_decimal.bind("<Return>", decimal_a_binario)
entry_decimal.bind("<KeyRelease>", limitar_entrada_decimal)

tk.Button(
    frame1, text="Convertir", command=decimal_a_binario, bg="#4e8cff", fg="white"
).pack(pady=5)

# =====================================================
# 2️⃣ Suma de Binarios (2 bits)
# =====================================================
frame2 = tk.LabelFrame(
    ventana,
    text="2️⃣ Suma de dos Binarios (2 bits)",
    bg="#2b2b40",
    fg="white",
    font=("Arial", 11, "bold"),
)
frame2.pack(padx=20, pady=10, fill="x")

tk.Label(frame2, text="Binario 1:", bg="#2b2b40", fg="white").pack()
entry_bin1 = tk.Entry(frame2, justify="center", font=("Arial", 12))
entry_bin1.pack(pady=3)
entry_bin1.bind("<Return>", sumar_binarios)
entry_bin1.bind("<KeyRelease>", lambda e: limitar_entrada_bin(entry_bin1, 2))

tk.Label(frame2, text="Binario 2:", bg="#2b2b40", fg="white").pack()
entry_bin2 = tk.Entry(frame2, justify="center", font=("Arial", 12))
entry_bin2.pack(pady=3)
entry_bin2.bind("<Return>", sumar_binarios)
entry_bin2.bind("<KeyRelease>", lambda e: limitar_entrada_bin(entry_bin2, 2))

tk.Button(frame2, text="Sumar", command=sumar_binarios, bg="#4e8cff", fg="white").pack(
    pady=5
)

# =====================================================
# 3️⃣ Binario a Código Gray (5 bits)
# =====================================================
frame3 = tk.LabelFrame(
    ventana,
    text="3️⃣ Binario a Código Gray (5 bits)",
    bg="#2b2b40",
    fg="white",
    font=("Arial", 11, "bold"),
)
frame3.pack(padx=20, pady=10, fill="x")

tk.Label(frame3, text="Binario (5 bits):", bg="#2b2b40", fg="white").pack()
entry_gray = tk.Entry(frame3, justify="center", font=("Arial", 12))
entry_gray.pack(pady=5)
entry_gray.bind("<Return>", binario_a_gray)
entry_gray.bind("<KeyRelease>", lambda e: limitar_entrada_bin(entry_gray, 5))

tk.Button(
    frame3, text="Convertir a Gray", command=binario_a_gray, bg="#4e8cff", fg="white"
).pack(pady=5)

# --- Pie de ventana ---
tk.Label(
    ventana,
    text="Desarrollado en Python 🐍 | Tkinter GUI",
    bg="#1c1c2e",
    fg="#999999",
    font=("Arial", 9),
).pack(side="bottom", pady=10)

# Iniciar la aplicación
ventana.mainloop()
