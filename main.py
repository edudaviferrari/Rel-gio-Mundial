from datetime import datetime
from pytz import country_timezones
import pytz

#importar lista dos paises
from paises import *

#Variavel com as areas
time_zones = pytz.all_timezones

#zonas com abreviação do país
timezone_country = {}
for countrycode in country_timezones:
    timezones = country_timezones[countrycode]
    for timezone in timezones:
        timezone_country[timezone] = countrycode

#Lista das zonas - Fuso Horários
zonas = []
for i in timezone_country.keys():
    zonas.append(i)

#Converter Zona selecionada no formato timezone
zona_selecionada = pytz.timezone(zonas[0])

#Obter hora da zona selecionada
country_time = datetime.now(zona_selecionada)

#Obter nome do país da zona selecionada
#Variavel que tera o simbolo do pais
simbol_do_pais = [timezone_country[zonas[56]]]

for i in paises.keys():
    simbol_do_pais.append(i.lower())

#usando format para obter o caminho da imagem (bandeira do pais)
imagem = "png250px/{}.{}".format(simbol_do_pais[0],'png')

#Obter key do país em letras maiusculas
key = simbol_do_pais[0].upper()

#obter nome do pais
nome_do_pais = paises[key]


print(f"A data da {zona_selecionada} é {country_time.strftime('%d-%m-%y')} e o país é {nome_do_pais} e la são {country_time.strftime('%H:%M:%S')}")