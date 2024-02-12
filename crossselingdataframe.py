import pandas as pd
import os
from itertools import combinations

# getting the current path, and set it to the available DataSet's path
currentpath = os.getcwd()
currentpath = currentpath+'\DataSet'

#orders table and we will just get let the necessary columns in that df
orderdf = pd.read_csv(f"{currentpath}\orders.csv")
orderdf = orderdf[["id","user_id"]]

#order_item table and we will just get let the necessary columns in that df
order_itemdf = pd.read_csv(f"{currentpath}\order_items.csv")
order_itemdf = order_itemdf[["order_id", "product_name"]]

# merging both
merged_df = orderdf.merge(order_itemdf, left_on='id', right_on='order_id', how='inner')

# dropping records where we can not find the product name or the user id
merged_df = merged_df.dropna(subset=['product_name', 'user_id'])


'''now making the df which is having two columns such as product, and purchased_with
for performing this i will use combination from itertools, lambda, and grooupby
'''

transactions = merged_df.groupby('user_id')['product_name'].apply(list)
product_combinations = pd.DataFrame([comb for sublist in transactions.apply(lambda x: list(combinations(x, 2))) for comb in sublist], columns=['product', 'purchased_with'])
top_pairs = product_combinations.groupby('product').apply(lambda x: x['purchased_with'].value_counts().idxmax())

# Convert the series to a DataFrame and reset the index
top_pairs_df = top_pairs.reset_index()
top_pairs_df.columns = ['product', 'purchased_with']
top_pairs_df.to_csv(currentpath+'/'+'relationship.csv')