import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Lire le fichier CSV
@st.cache_data
def load_data():
    df = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')
    return df

df = load_data()

st.title("L'automobile dans le monde...")

# Ajouter un sélecteur pour choisir le continent
continent = st.sidebar.selectbox('Choisissez un continent', df['continent'].unique())

# Filtrer les données en fonction du continent sélectionné
df = df[df['continent'] == continent]

# Afficher les premières lignes du DataFrame pour vérifier que les données ont été correctement lues
st.write(df.head())

# Créer une matrice de corrélation pour les colonnes numériques uniquement
numeric_cols = df.select_dtypes(include=[np.number]).columns
corr_matrix = df[numeric_cols].corr()

# Afficher la matrice de corrélation avec Seaborn
fig, ax = plt.subplots()
sns.heatmap(corr_matrix, annot=True, ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
sns.scatterplot(data=df, x='weightlbs', y='hp', hue='continent', ax=ax)
plt.xlabel('Poids (lbs)')
plt.ylabel('Puissance (hp)')
plt.title('Poids vs Puissance par Région')
st.pyplot(fig)

st.write("""
Ce graphique montre la relation entre le poids et la puissance des véhicules pour différentes régions. 
On peut observer que les véhicules des États-Unis ont tendance à être plus lourds et plus puissants, 
tandis que les véhicules du Japon et de l'Europe sont généralement plus légers et moins puissants. 
Cela pourrait être dû à des différences dans les préférences des consommateurs ou dans les réglementations environnementales entre ces régions.
""")