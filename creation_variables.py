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
# goods_code1 A goods_code24 (CHAR) 	Code de l'item 1 à 24 	2378284364 
# NBR_OF_PROD_PURCHAS1 À NBR_OF_PROD_PURCHAS24 (NUM) 	Nombre de produits dans l'item 1 à 24 	2 
# Nb_of_items(NUM) 	Nombre total d'items 	7 

# Enlever goods_code
for i in range(1, 25):
    train = train.drop(columns=[f'goods_code{i}'])
    test = test.drop(columns=[f'goods_code{i}'])

## Création de variables

# Prix total par items : Prix de chaque item multiplié par le nombre d'items
for i in range(1, 25):
    train[f'TOTAL_PRICE{i}'] = train[f'cash_price{i}'] * train[f'Nbr_of_prod_purchas{i}']
    test[f'TOTAL_PRICE{i}'] = test[f'cash_price{i}'] * test[f'Nbr_of_prod_purchas{i}']

# Prix total de tous les items
train['TOTAL_PRICE'] = train[[f'TOTAL_PRICE{i}' for i in range(1, 25)]].sum(axis=1)
test['TOTAL_PRICE'] = test[[f'TOTAL_PRICE{i}' for i in range(1, 25)]].sum(axis=1)

# Moyenne des prix par item : TOTAL_PRICE divisé par Nb_of_items 
train['MEAN_PRICE'] = train['TOTAL_PRICE'] / train['Nb_of_items']
test['MEAN_PRICE'] = test['TOTAL_PRICE'] / test['Nb_of_items']

# enregistrer en CSV
train.to_csv('data/X_train_variables.csv', index=False)
test.to_csv('data/X_test_variables.csv', index=False)

