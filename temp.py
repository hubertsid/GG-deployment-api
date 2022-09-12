import sqlite3

conn_new = sqlite3.connect("img.db")
c_new = conn_new.cursor()
query = 'CREATE TABLE games(id INT NOT NULL UNIQUE, title TEXT NOT NULL UNIQUE, url TEXT, img TEXT)'
c_new.execute(query)



conn = sqlite3.connect("game.db")
c = conn.cursor()
query = "SELECT * FROM games"
c.execute(query)
results = c.fetchall()

counter = 1
for res in results:
    id = res[2].replace("https://store.steampowered.com/app/","").replace("/","").lstrip()
    url = "https://cdn.akamai.steamstatic.com/steam/apps/"+id+"/header.jpg"
    query = 'INSERT INTO games VALUES(?,?,?,?)'

    c_new.execute(query, (counter, res[1], res[2], url))
    conn_new.commit()
    counter += 1

    




# from matplotlib.pyplot import text
# import requests
# from bs4 import BeautifulSoup
# import json

# url = "https://www.google.com/search?q=Stray&sxsrf=ALiCzsbCZjw1e170whSX9Fq9lOH7BlQvwQ:1657892288418&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiB77SHgvv4AhUJt4sKHRkkDPwQ_AUoAXoECAIQAw&biw=1745&bih=881&dpr=1.1"

# def get_data(url):
#     r = requests.get(url)
#     return r

# def parse(data):
#     soup = BeautifulSoup(data, 'html.parser')
#     return soup

# def extract_game_data(soup):
#     #get image class
#     img_class = soup.find('img', {'class' : 'yWs4tf'})
    
#     print(img_class['src'])  

# data = get_data(url)
# soup = parse(data.content)
# extract_game_data(soup)