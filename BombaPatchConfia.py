#----------------- Importação -----------------
import customtkinter as cstk
from tkinter import messagebox
import os
os.system('cls')
#----------------- Janela -----------------

cstk.set_appearance_mode('White')

janela = cstk.CTk('Black')
janela.geometry('600x400')
janela.title('Bomba patch v9.6 2024 atualizado by AnjoCaido')
janela.resizable(width=False,height=False)

cstk.CTkLabel(janela,
                       text='Bomba Patch',
                       font=('Comic Sans MC', 40, 'bold',), 
                        text_color='white').pack(pady=20)
#----------------- Funções -----------------
def logoff():
    os.system('shutdown -l ')
    
def desligar():
    os.system('shutdown -s -t 0')

def reiniciar():
    os.system('shutdown -r -t 0')

#----------------- Botões -----------------

desligar = cstk.CTkButton(janela,
                        width=150,
                        height=30,
                        corner_radius=500,
                        fg_color='Red',
                        text='Desligar',
                        text_color='#000000',
                        cursor="hand2",
                        hover_color='#a81e1e',
                        font=('Comic Sans MC', 15, 'bold'),
                        command=desligar)
desligar.pack(pady=20)

reiniciar = cstk.CTkButton(janela,
                        width=150,
                        height=30,
                        corner_radius=100,
                        fg_color='Orange',
                        text='reiniciar',
                        text_color='#000000',
                        cursor='hand2',
                        font=('Comic Sans MC', 15, 'bold'),
                        hover_color='#db991d',
                        command=reiniciar)
reiniciar.pack(pady=20)

bloquear = cstk.CTkButton(janela,
                        width=150,
                        height=30,
                        corner_radius=500,
                        fg_color='Green',
                        text='bloquear',
                        text_color='#000000',
                        font=('Comic Sans MC', 15, 'bold'),
                        cursor='pirate',
                        hover_color='#43b32d',
                        command=logoff)
bloquear.pack(pady=20)



janela.mainloop()
