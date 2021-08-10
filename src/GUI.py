import sali
from tkinter import *

sali = sali.Sali()


def calcular():
    salario = float(input.get())
    print(salario)
    inss = sali.inss_calc(salario)
    ir = sali.irrf_calc(salario - inss)
    liq = round(salario - inss - ir, 2)
    print(liq)
    resultado.set(f"Salário Líquido: {liq}")


janela = Tk()
janela.geometry("400x300")
janela.title("Calculo de salário líquido com MSC")

prompt = Label(janela, font=("Helvetica", 20), text="Salário bruto:")
prompt.grid(column=0, row=0)

input = Entry()
input.grid(column=1, row=0)

button = Button(text="calcular", command=calcular)
button.grid(column=1, row=2)

resultado = StringVar()
label_resultado = Label(janela, font=("Helvetica", 20), textvariable=resultado)
label_resultado.grid(column=1, row=3)

janela.mainloop()
