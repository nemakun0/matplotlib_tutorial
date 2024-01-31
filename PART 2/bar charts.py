import csv
from matplotlib import pyplot as plt
from collections import Counter
import numpy as np
import pandas as pd

plt.style.use("fivethirtyeight")

data = pd.read_csv("data.csv")
ids= data["Responder_id"]
lang_responses = data['LanguagesWorkedWith']

lanuage_counter = Counter() 

for response in lang_responses:
    language_counter.update(response['LanguagesWorkedWith'].split(';'))
    
languages = []
popularity = []


for item in language_counter.most_common(15):
    languages.append(item[0])#tuple şeklinde bölünmüş olan verinin ilk elemanını diziye kaydetti
    popularity.append(item[1])#tuple şeklinde bölünmüş olan verinin 2. elemanını diziye kaydetti

language.reverse()
popularity.reverse()

plt.barh(languages,popularity)# horizontal/yatay grafik oluşturur.bundan dolayı x ve y nin yerlerini değiştirdik

plt.title("Most Popular Languages")
plt.ylabel("Programming Languages")
plt.xlabel("Number Of People Who Use")

plt.tight_layout()

plt.show()



