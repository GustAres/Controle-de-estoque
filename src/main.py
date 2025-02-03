from src.controllers.gestao import *
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"G:\Projeto\Controle de estoque\src\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def atualizar_tela():
    button_1.place_forget()

    canvas.delete("all")

    canvas.create_text(
        640, 360,
        text="Nova Tela Atualizada!",
        fill="#FFFFFF",
        font=("Manuale Regular", 30 * -1)
    )

    button_voltar = Button(
        window,
        text="Voltar",
        command=voltar_tela,
        relief="flat"
    )
    canvas.create_window(640, 450, window=button_voltar)


def voltar_tela():
    canvas.delete("all")

    canvas.create_image(
        598.0,
        360.0,
        image=image_image_1
    )
    canvas.create_text(
        22.0,
        61.0,
        anchor="nw",
        text="Aplicativo de Estoque",
        fill="#007FB5",
        font=("Manuale Regular", 30 * -1)
    )

    button_1.place(
        x=26.0,
        y=154.0,
        width=268.0,
        height=65.0
    )


window = Tk()
window.geometry("1280x720")
window.configure(bg="#007FB5")

canvas = Canvas(
    window,
    bg="#007FB5",
    height=720,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
canvas.create_image(
    598.0,
    360.0,
    image=image_image_1
)

canvas.create_text(
    22.0,
    61.0,
    anchor="nw",
    text="Aplicativo de Estoque",
    fill="#007FB5",
    font=("Manuale Regular", 30 * -1)
)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    window,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=atualizar_tela,  # Atualiza a tela ao clicar
    relief="flat"
)
button_1.place(
    x=26.0,
    y=154.0,
    width=268.0,
    height=65.0
)

window.resizable(False, False)
window.mainloop()
