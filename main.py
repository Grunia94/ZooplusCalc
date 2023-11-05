from bs4 import BeautifulSoup
import requests
import json
import sqlite3


values=list()
ingredient_dict = {}

links = []
_links = []

# Pobierz zawartość strony internetowej

conn = sqlite3.connect(r'D:\Baza\citcalc.db')
cursor = conn.cursor()
cursor.execute('''
                DELETE FROM ZooplusNutritions               
            ''')
conn.commit()
cursor.close()

for i in range(1,100):
    url= "https://www.zooplus.pl/shop/koty/karma_dla_kota_mokra?p=" + str(i)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")

    script = soup.find_all('script')[5].text.strip()
    json_obj = json.loads(script)
    articles2 = json_obj['itemListElement']

    for _iter in articles2:
        links.append(_iter.get('url'))

for urls in links:
        response = requests.get(urls)
        soup = BeautifulSoup(response.text, features="html.parser")

        script = soup.find_all('script')[34].text.strip()
        json_obj = json.loads(script)
        articles = json_obj['props']['pageProps']['pageLevelProps']['pdpContext']['product']['articleVariants']

        attributes = ['Id', 'Marka', 'Nazwa', 'Białko surowe', 'Tłuszcz surowy', 'Włókno surowe', 'Popiół surowy',
                      'Wapń', 'Fosfor', 'Wilgotność', 'Potas', 'Sód', 'Kwasy tłuszczowe Omega 3',
                      'Kwasy tłuszczowe Omega 6']
        articles_name = json_obj['props']['pageProps']['pageLevelProps']['pdpContext']['product']['brand']

        for i in articles:
            _id_num = i.get('id')
            _name = i.get('description')
            _artname = str(articles_name)
            foods = i.get('articleConstituents')
        for item in foods:
            ingredient_dict['Id'] = [_id_num]
            ingredient_dict['Marka'] = [_artname]
            ingredient_dict['Nazwa'] = [_name]
            ingredient_name = item['ingredientName']
            amount = item['amount']
            if ingredient_name in ingredient_dict:
                ingredient_dict[ingredient_name].append(amount)
            else:
                ingredient_dict[ingredient_name] = [amount]
            values = [ingredient_dict.get(atribute, [0])[0] for atribute in attributes]
        print(values)
        # na tym poziomie zrobić obsługę bazy
        conn = sqlite3.connect(r'D:\Baza\citcalc.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ZooplusNutritions (
                Id INT PRIMARY KEY,
                Brand TEXT,
                Name TEXT,
                Protein FLOAT,
                Fat FLOAT,
                Fiber FLOAT,
                Calx FLOAT,
                Calcium FLOAT,
                Phosphorus FLOAT,
                Humidity FLOAT,
                Potassium FLOAT,
                Sodium FLOAT,
                Omega3 FLOAT,
                Omega6 FLOAT
            )               
        ''')
        if ingredient_dict:
            cursor.execute('''INSERT OR IGNORE INTO ZooplusNutritions
             (Id, Brand, Name, Protein, Fat, Fiber, Calx, Calcium, Phosphorus, Humidity, Potasium, Sodium, Omega3, Omega6)
              VALUES (?, ?, ?, ?, ? , ?, ?, ?, ? , ?, ?, ?, ?, ?)'''
                           , (values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7],
                              values[8], values[9], values[10], values[11], values[12], values[13]))
            conn.commit()
            cursor.close()
        ingredient_dict = {}
