import mysql.connector
import pandas as pd
import os
import numpy as np
import time
current_path = os.getcwd() + '/' 'DataSet' 


def Inventory_df():
    '''
    This function is used to return the inventory df for analysis purpose.
    This function is including the details of the stock, order_count, product_name, etc..
    '''
    db = mysql.connector.connect(
    host="localhost",  
    user="root",  
    password="rootroot",  
    database="interview"
    )


    query = '''
                SELECT ppi.product_id, ppi.stock, ppi.active_stock, oi.product_name, COUNT(oi.product_id) as ordered_stock
                FROM products_pricing_inventory ppi
                LEFT JOIN order_items oi ON ppi.product_id = oi.product_id
                GROUP BY ppi.product_id, ppi.stock, ppi.active_stock, oi.product_name
            '''

    inventory_monetoring_df = pd.read_sql_query(query,db)

    return inventory_monetoring_df
    
inventory_monetoring_df = Inventory_df()

# dropping the null value records from the dataframe
inventory_monetoring_df = inventory_monetoring_df.dropna()

# now adding the three columns names days, and velocity, and reoder
inventory_monetoring_df['days'] = np.nan
inventory_monetoring_df['velocity'] = np.nan
inventory_monetoring_df['reoder_basedon_stock'] = np.nan
inventory_monetoring_df['reoder_basedon_available_stock'] = np.nan

productid = inventory_monetoring_df['product_id']
uniquelst = list(set(inventory_monetoring_df['product_id']))

# now for each uniqueproduct we will find the days and make a key value pair of dict
df = pd.read_csv(current_path+'/'+'order_items.csv')
df['created_at'] = pd.to_datetime(df['created_at'], format='%Y-%m-%d %H:%M:%S').dt.date
for productid in uniquelst:
    _df = df[df["product_id"] == productid]
    datelist = list(set(_df['created_at']))
    inventory_monetoring_df.loc[inventory_monetoring_df['product_id'] == productid, 'days'] = len(datelist)
    

# now finding the velocity of each product
# formula for the velocity is  stock/days
inventory_monetoring_df['velocity'] = inventory_monetoring_df['ordered_stock']/inventory_monetoring_df['days']

#formula for reorder
#velocity*20(timespan for analysis) - stock
inventory_monetoring_df['reoder_basedon_stock'] = inventory_monetoring_df['velocity']*20- inventory_monetoring_df['stock']
inventory_monetoring_df['reoder_basedon_available_stock'] = inventory_monetoring_df['velocity']*20- inventory_monetoring_df['active_stock']


# now where we have the -negative reorder means we do not require to order in that product as we have sufficient stocks available
# now we want to make the negative to 0, as we fo not want to order fuue to stock available for the 20dayas
# we also need to round we can not order the half portion of the product.
inventory_monetoring_df['reoder_basedon_stock'] = inventory_monetoring_df['reoder_basedon_stock'].clip(lower=0).round()
inventory_monetoring_df['reoder_basedon_available_stock'] = inventory_monetoring_df['reoder_basedon_available_stock'].clip(lower=0).round()
inventory_monetoring_df.to_csv(current_path+'/'+"inventory_monetoring.csv")

