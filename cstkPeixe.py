#------------ Importação ------------
import customtkinter as cstk
import os
from tkinter import messagebox
os.system('cls')

#------------ Janela ------------
cstk.set_appearance_mode('System')
janela = cstk.CTk()
janela.geometry('800x600')
janela.title('Calculo de Multa')
janela.resizable(width=False, height=False)

#------------ Definindo a função de multa ------------
def total_multa():
    multa = 4
    q= int(quilo.get())
    valor_total = (q-50)*multa
    if valor_total<0 or valor_total==0:
        messagebox.showinfo('Multa', f'Nenhuma multa foi aplicada')
    else:
        messagebox.showinfo('Valor final:', f'O gasto será de: R${valor_total:.2f}')

#------------ Formato da Janela ------------
cstk.CTkLabel(janela,
            text=('Calculadora da multa '),
            font=('Verdana', 30, 'bold'),
            text_color='White').pack(pady=15)

#------------ Entrada do Quilo ------------
quilo = cstk.CTkEntry(janela,
                    width=300,
                    height=30,
                    border_width=3,
                    corner_radius=100,
                    placeholder_text=('Quantos quilos de peixe você pegou?'),
                    text_color='White')
quilo.pack()

#------------ Botão de calculo ------------
botao = cstk.CTkButton(janela,
                    width=100,
                    height=15,
                    corner_radius=500,
                    fg_color='Cyan',
                    text='Calcular',
                    text_color='Black',
                    cursor='hand2',
                    hover_color='#57e6e1',
                    command=total_multa)
botao.pack(pady=5)

#------------ resultado ------------
resultado = cstk.CTkLabel(janela,
                        text='',
                        font=('Calibri', 20, 'bold',),
                        text_color='White')
resultado.pack(pady=10)

janela.mainloop()
