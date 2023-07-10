import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import pdfplumber
import operator


def filtrar_dados_pdf(caminho_arquivo):
    dados_filtrados = []
    with pdfplumber.open(caminho_arquivo) as pdf:
        for page in pdf.pages:
            text_content = page.extract_text()
            items = text_content.strip().split("\n")

            for item in items:
                if "PEPSI" in item:
                    descricao = item
                    dados_filtrados.append({"descricao": descricao})

    dados_filtrados.sort(key=lambda x: x["descricao"])
    return dados_filtrados


def exibir_resultado():
    caminho_pdf = "./Oasis.pdf"
    dados_filtrados = filtrar_dados_pdf(caminho_pdf)

    window = tk.Tk()
    window.title("Resultado")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    window_width = int(screen_width * 0.6)
    window_height = int(screen_height * 0.6)

    x = int((screen_width - window_width) / 2)
    y = int((screen_height - window_height) / 2)

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    text = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Arial", 10))
    text.pack(fill=tk.BOTH, expand=True)

    text.tag_configure("center", justify="center")
    text.insert(tk.END, "\n")
    text.tag_add("center", "1.0", "end")

    for dado in dados_filtrados:
        descricao = dado["descricao"]
        text.insert(tk.END, f"Descrição: {descricao}\n\n", "center")

    window.mainloop()


exibir_resultado()
