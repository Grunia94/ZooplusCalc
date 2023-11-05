#Do użycia na później
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
