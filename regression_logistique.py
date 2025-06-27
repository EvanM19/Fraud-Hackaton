import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import kruskal
import seaborn as sns
from scipy.stats import chi2_contingency
import numpy as np

train = pd.read_csv('data/X_train_variables.csv')
test = pd.read_csv('data/X_test_variables.csv')

# Séparer les groupes en fonction de la variable cible binaire
group_0 = train[train['target'] == 0]
group_1 = train[train['target'] == 1]

qualitatives_cols = [f"item{i}" for i in range(1, 25)] + [f"make{i}" for i in range(1, 25)] + [f"model{i}" for i in range(1, 25)] + ['target']
quantitative_cols = [f"cash_price{i}" for i in range(1, 25)] + [f"Nbr_of_prod_purchas{i}" for i in range(1, 25)] + ['Nb_of_items'] + [f'TOTAL_PRICE{i}' for i in range(1, 25)] + ['TOTAL_PRICE'] + ['MEAN_PRICE']

# On remplacer les valeurs manquantes des variables quantitatives par 0
train[quantitative_cols] = train[quantitative_cols].fillna(0)
test[quantitative_cols] = test[quantitative_cols].fillna(0)

# Dictionnaire pour stocker les résultats
results = {}

# Appliquer le test de Kruskal-Wallis à chaque variable quantitative
for col in quantitative_cols:
    stat, p_value = kruskal(group_0[col], group_1[col])
    results[col] = {'Statistique': stat, 'p-value': p_value}

# Convertir le dictionnaire de résultats en DataFrame
results_df = pd.DataFrame(results).T

# Trier les résultats par la statistique du test (Statistique) de manière croissante
results_df_sorted = results_df.sort_values(by='Statistique', ascending=True)

# Filtrer les variables avec des p-value < 0.05 (significatives)
significant_results = results_df_sorted[results_df_sorted['p-value'] < 0.05]

# Créer un diagramme en barres des statistiques de Kruskal-Wallis pour les variables significatives
plt.figure(figsize=(10, 6))
plt.barh(significant_results.index, significant_results['Statistique'], color='skyblue', edgecolor='black')
plt.xlabel('Statistique Kruskal-Wallis')
plt.ylabel('Variables Quantitatives')
plt.title('Diagramme en Barres des Statistiques de Kruskal-Wallis pour les Variables Significatives')
plt.grid(True, axis='x', linestyle='--', alpha=0.7)
plt.show()

#######

quantitative_cols_after_wallis = []

df = train[quantitative_cols_after_wallis]

# Calcul de la corrélation de Pearson
pearson_corr = df.corr(method='pearson')

# Plot de la heatmap pour la corrélation de Pearson
plt.figure(figsize=(12, 8))
sns.heatmap(pearson_corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Heatmap - Corrélation de Pearson')
plt.show()