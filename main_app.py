from tkinter.ttk import *
from tkinter import*
from tkinter import Tk, StringVar, ttk

#Biblioteca Pillow
from PIL import Image, ImageTk

#Importando Zonas
from datetime import datetime
from pytz import country_timezones 
import pytz

#importando tipo de letra
import pyglet
pyglet.font.add_file('digital-7.ttf')

#Importando Paises
from paises import *


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

# Abrir imagem
app_img = Image.open('./icon.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima,image=app_img, text=' Relógio Mundial', width=920, compound=LEFT, relief=FLAT, anchor=NW, font=('digital-7 25'), bg=cor1, foreground=cor0)
app_logo.place(x=0, y=0)

frameDireita_conteudo_0 = Frame(frameDireita, width=300, height=35, bg=cor1, relief=RAISED)
frameDireita_conteudo_0.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

frameDireita_conteudo_1 = Frame(frameDireita, width=300, height=155, bg=cor1, relief=FLAT)
frameDireita_conteudo_1.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#Codigo para obter as zonas de fuso horario --------
#zonas com abreviação do país
timezone_country = {}
for countrycode in country_timezones:
    timezones = country_timezones[countrycode]
    for timezone in timezones:
        timezone_country[timezone] = countrycode

# Lista das zonas - Fuso Horários
zonas = []

for i in timezone_country.keys():
    zonas.append(i)

# FUNÇÕES -------------
#Variaveis Globais
global l_icon, img_bandeira

def relogio():
    global l_icon, img_bandeira

    zona = c_zona.get()

    #convertendo a zona seleciona no formato timezone
    zona_selecionada = pytz.timezone(zona)

    #Obter hora da zona selecionada
    country_time = datetime.now(zona_selecionada)

    #Obter nome do país da zona selecionada
    #Variavel que tera o simbolo do pais
    simbol_do_pais = [timezone_country[zona]]

    for i in paises.keys():
        simbol_do_pais.append(i.lower())

    #usando format para obter o caminho da imagem (bandeira do pais)
    imagem = "./png250px/{}.{}".format(simbol_do_pais[0],'png').lower()

    #Obter key do país em letras maiusculas
    key = simbol_do_pais[0].upper()

    #obter nome do pais
    nome_do_pais = paises[key]

    tempo = country_time
    horas = tempo.strftime("%H:%M:%S")
    dia_da_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%B")
    ano = tempo.strftime("%Y")
    periodo = tempo.strftime("%p")

    #Passar dados pelas Labels
    l_cidade.config(text=zona)
    l_pais.config(text=nome_do_pais)
    l_horas.config(text=horas)
    l_data.config(text=dia_da_semana + ", "+ "" + str(dia) + " " + str(mes) + " " + (ano) + " " + (periodo))
    l_periodo.config(text=(periodo))

    #imagem bandeira
    img_bandeira = Image.open(imagem)
    img_bandeira = img_bandeira.resize((105, 64))
    img_bandeira = ImageTk.PhotoImage(img_bandeira)

    l_icon = Label(frameDireita_conteudo_1, image=img_bandeira, bg=cor0, relief='solid')
    l_icon.place(x=185, y=25)

    #Reset Função a cada 1 segundo
    l_horas.after(200, relogio)

# Trabalhando no frame conteudo 1 ----------------------------

l_zona = Label(frameDireita_conteudo_0, text="Fuso Horário *", width=35, height=1, anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor0)
l_zona.place(x=10, y=10)

c_zona = Combobox(frameDireita_conteudo_0, width=25)
# Recebendo Zonas
c_zona['values']= (zonas)
c_zona.set('America/Sao_Paulo')
c_zona.place(x=123, y=10)

#Trabalhando no frame conteudo 2 ------------------------

l_cidade = Label(frameDireita_conteudo_1, text='New York', anchor=NW, font=('Arial 10'), bg=cor1, fg=cor0)
l_cidade.place(x=10,y=8)
l_pais = Label(frameDireita_conteudo_1, text='USA', anchor=NW, font=('Arial 10'), bg=cor1, fg=cor2)
l_pais.place(x=10, y=28)
l_horas = Label(frameDireita_conteudo_1, text="10:05:05", font=('digital-7 25 bold'), bg=cor1, fg=cor2)
l_horas.place(x=10, y=45)
l_periodo = Label(frameDireita_conteudo_1, text='PM', anchor=NW, font=('Verdana 10'), bg=cor1, fg=cor2)
l_periodo.place(x=145, y=60)
l_data = Label(frameDireita_conteudo_1, font=('Arial 8'), bg=cor1, fg=cor0)
l_data.place(x=10, y=79)


# imagem bandeira
# img_bandeira = Image.open('./png250px/br.png')
# img_bandeira = img_bandeira.resize((93, 55))
# img_bandeira = ImageTk.PhotoImage(img_bandeira)

# l_icon = Label(frameDireita_conteudo_1, image=img_bandeira, bg=cor1, relief='solid')
# l_icon.place(x=180, y=40)

#Executar a funcção Relogio
relogio()
janela.mainloop()