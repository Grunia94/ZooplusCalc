from bs4 import BeautifulSoup
import requests 
import xlsxwriter
import re
import math

headers=list()
values=list()

waga=float(input("Podaj wagę: "))


response = requests.get("https://www.zooplus.pl/shop/koty/karma_dla_kota_mokra/granatapet/1889536")
soup = BeautifulSoup(response.text,features="html.parser")


table = soup.find('table', {"data-zta": "constituentsTable"})
for i, row in enumerate(table.find_all('tr')):
        values.append([el.text.strip() for el in row.find_all('td')])
# Inicjalizacja pustego słownika
variable_dict = {}

# Przetwarzanie listy i przypisywanie zmiennych i wartości jako liczby zmiennoprzecinkowe (float)
for item in values:
    variable_name, value_str = item
    # Użyj wyrażenia regularnego do wyłuskania cyfr i kropki dziesiętnej
    matches = re.findall(r'[0-9.]+', value_str)
    if matches:
        value_float = round(float(matches[0]), 4)
        variable_dict[variable_name] = value_float

# Wydrukowanie utworzonego słownika
for key, value in variable_dict.items():
    print(f'{key}: {value}')
bialko_surowe = variable_dict.get('Białko surowe', None)
tluszcz_surowy = variable_dict.get('Tłuszcz surowy', None)
wlokno_surowe = variable_dict.get('Włókno surowe', None)
popiol_surowy = variable_dict.get('Popiół surowy', None)
wapn = variable_dict.get('Wapń', None)
fosfor = variable_dict.get('Fosfor', None)
wilgotnosc = variable_dict.get('Wilgotność', None)
potas = variable_dict.get('Potas', None)
sod = variable_dict.get('Sód', None)
omega_3 = variable_dict.get('Kwasy tłuszczowe Omega 3', None)
omega_6 = variable_dict.get('Kwasy tłuszczowe Omega 6', None)

# Przypisz wartości do pojedynczych zmiennych
if bialko_surowe is not None:
    print(f'Białko surowe: {bialko_surowe} %')
if tluszcz_surowy is not None:
    print(f'Tłuszcz surowy: {tluszcz_surowy} %')
if wlokno_surowe is not None:
    print(f'Włókno surowe: {wlokno_surowe} %')
if popiol_surowy is not None:
    print(f'Popiół surowy: {popiol_surowy} %')
if wapn is not None:
    print(f'Wapń: {wapn} %')
if fosfor is not None:
    print(f'Fosfor: {fosfor} %')
if wilgotnosc is not None:
    print(f'Wilgotność: {wilgotnosc} %')
if potas is not None:
    print(f'Potas: {potas} %')
if sod is not None:
    print(f'Sód: {sod} %')
if omega_3 is not None:
    print(f'Kwasy tłuszczowe Omega 3: {omega_3} %')
if omega_6 is not None:
    print(f'Kwasy tłuszczowe Omega 6: {omega_6} %')

# Wyświetl przypisane wartości
print(f'Białko surowe: {bialko_surowe} %')
print(f'Tłuszcz surowy: {tluszcz_surowy} %')
print(f'Włókno surowe: {wlokno_surowe} %')
print(f'Popiół surowy: {popiol_surowy} %')
print(f'Wapń: {wapn} %')
print(f'Fosfor: {fosfor} %')
print(f'Wilgotność: {wilgotnosc} %')
print(f'Potas: {potas} %')
print(f'Sód: {sod} %')
print(f'Kwasy tłuszczowe Omega 3: {omega_3} ')
print(f'Kwasy tłuszczowe Omega 6: {omega_6} ')

# Procentowa wartosc weglowodanow w mokrej masie
pww = round((100 - bialko_surowe - tluszcz_surowy - popiol_surowy - wlokno_surowe - wilgotnosc), 2)
print('Procentowa wartosc weglowodanow w mokrej masie: ',pww)
# Gęstość energetyczna karmy
gek = round((bialko_surowe*3.5)+(tluszcz_surowy*8.5)+(pww*3.5),2)
print('Gęstość energetyczna karmy: ', gek)
# Rozmieszczenie energii w karmie
rek = round((((bialko_surowe * 3.5) / ((bialko_surowe*3.5)+(tluszcz_surowy*8.5)+(pww*3.5))) * 100),2)
print('Rozmieszczenie energii w karmie: ', rek)
# Dzienne zapotrzebowanie (MER)
mer= round((60 * (math.pow(waga, 0.67))),2)
print('Dzienne zapotrzebowanie [kcal/dzien]: ',mer)
# Dzienna dawka pokarmowa [g/dzien]
ddp= round((((60 * (math.pow(waga, 0.67)))/((bialko_surowe*3.5)+(tluszcz_surowy*8.5)+(pww*3.5))) * 100),2)
print('Dzienna dawka pokarmowa [g/dzien]: ',ddp)
# Procent bialka w suchej masie
pbs = round(((bialko_surowe / (100 - wilgotnosc)) * 100),2)
print('Procent bialka w suchej masie: ',pbs)
# Procent tłuszczu w suchej masie
pts= round((tluszcz_surowy / (100 - wilgotnosc) * 100),2)
print('Procent tłuszczu w suchej masie: ', pts)
# Procent weglowodanów w suchej masie
pws= round((pww/(100-wilgotnosc)*100),2)
print('Procent weglowodanów w suchej masie: ',pws)
# Procent wapnia w suchej masie
pwas = round(100 * ( wapn / (100 - wilgotnosc )),2)
print('Procent wapnia w suchej masie: ',pwas)
# Procent fosforu w suchej masie
pfs = round(100 * ( fosfor / (100 - wilgotnosc )),2)
print('Procent fosforu w suchej masie: ',pfs)
# Zapotrzebowanie na wodę [ml]
znw= round((50*waga),2)
print('Zapotrzebowanie na wodę [ml]: ',znw)