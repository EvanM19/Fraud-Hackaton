import pandas as pd

train = pd.read_csv('data/X_train.csv')
test = pd.read_csv('data/X_test.csv')

# Format des données: 

# Variable 	Description 	Exemple 
# ID (NUM) 	Identifiant unique 	1 
# ITEM1 A ITEM24 (CHAR) 	Catégorie du bien de l'item 1 à 24 	Computer 
# CASH_PRICE1 A CASH_PRICE24 (NUM) 	Prix de l'item 1 à 24 	850 
# MAKE1 A MAKE24 (CHAR) 	Fabriquant de l'item 1 à 24 	Apple 
# MODEL1 A MODEL24 (CHAR) 	Description du modèle de l'item 1 à 24 	Apple Iphone XX 
# GOODS_CODE1 A GOODS_CODE24 (CHAR) 	Code de l'item 1 à 24 	2378284364 
# NBR_OF_PROD_PURCHAS1 À NBR_OF_PROD_PURCHAS24 (NUM) 	Nombre de produits dans l'item 1 à 24 	2 
# NB_OF_ITEMS (NUM) 	Nombre total d'items 	7 

# Enlever GOODS_CODE
train = train.drop(columns=['GOODS_CODE'])
test = test.drop(columns=['GOODS_CODE'])

# Création de variables

# Prix total par items : Prix de chaque item multiplié par le nombre d'items
for i in range(1, 25):
    train[f'TOTAL_PRICE{i}'] = train[f'CASH_PRICE{i}'] * train[f'NBR_OF_PROD_PURCHAS{i}']
    test[f'TOTAL_PRICE{i}'] = test[f'CASH_PRICE{i}'] * test[f'NBR_OF_PROD_PURCHAS{i}']