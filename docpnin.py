# importer les bibliothèques 
import requests
import pandas as pd
from bs4 import BeautifulSoup




# URL du site web
url = "https://pnin-niger.org/web/publications-et-documentation/"

# recupérer la page html
reponse  = requests.get(url)
soup = BeautifulSoup(reponse.content, 'html.parser')

# Trouver le tableau
table = soup.find('table', {'class': 'posts-data-table'})

# Initialiser les listes pour stocker les données
titres = []
dates = []
liens = []

# Parcourir chaque ligne du tableau
for ligne in table.find('tbody').find_all('tr'):
    # Extraire les colonnes
    cell_titre = ligne.find('td')
    cell_date = ligne.find('td', {'data-sort': True})
    cell_lien = ligne.find('a', {'class': 'document-library-pro-button'})
    # Ajouter les données aux listes
    titres.append(cell_titre.text.strip())
    dates.append(cell_date.text.strip())
    liens.append(cell_lien['href'])

# Convertir les données en DataFrame pandas
donnees = pd.DataFrame({
    'Titre': titres,
    'Date de publication': dates,
    'Lien': liens
})

# Sauvegarder dans un fichier csv
donnees.to_csv("documents.csv", index=False, encoding='utf-8')
donnees.to_excel("docs.xlsx", index=False)

