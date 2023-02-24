from tkinter.ttk import *
from tkinter import*
from tkinter import Tk, StringVar, ttk

#Biblioteca Pillow
from PIL import Image, ImageTk

#Cores
cor0 = "#2e2d2b" #Preta
cor1 = "#feffff" #Branca
cor2 = "#34c6eb" #Azul
cor3 = "#38576b" #Valor

#Janela
janela = Tk()
janela.title('Relógio Mundial')
janela.geometry('300x190')
janela.configure(background=cor3)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

#FRAMES
frameCima = Frame(janela, width=300, height=50, bg=cor1, relief=FLAT)
frameCima.grid(row=0, column=0, columnspan=2)

frameDireita = Frame(janela, width=300, height=390, bg=cor0, relief=FLAT)
frameDireita.grid(row=1, column=0, pady=1,padx=0, sticky=NSEW)

frameDireita_conteudo_0 = Frame(frameDireita, width=300, height=35, bg=cor1, relief=RAISED)
frameDireita_conteudo_0.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

frameDireita_conteudo_1 = Frame(frameDireita, width=300, height=155, bg=cor1, relief=FLAT)
frameDireita_conteudo_1.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#Abrir imagem
app_img = Image.open('./icon.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima,image=app_img, text=' Relógio Mundial', width=920, compound=LEFT, relief=FLAT, anchor=NW, font=('digital-7 25'), bg=cor1, foreground=cor0)
app_logo.place(x=0, y=0)

# Trabalhando no frame conteudo 1 ----------------------------
l_zona = Label(frameDireita_conteudo_0, text="Fuso Horário *", width=35, height=1, anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor0)
l_zona.place(x=10, y=10)

c_zona = Combobox(frameDireita_conteudo_0, width=25)
#Recebendo Zonas
c_zona.set('Asia/Kolkata')
c_zona.place(x=123, y=10)

janela.mainloop()