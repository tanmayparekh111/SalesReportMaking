from GetData import FatchData, FatchTables
import os
'''
we have this 6 tables
businesses
locations
order_items
orders
products
products_pricing_inventory
now we are making the csv just to look at the how the data is formulated over the different table
'''
# storing evevry 6 tables into the csv file to analyze manually, to evaluate the necessary items in the given dataset.
TableNames = FatchTables()

currentpath = os.getcwd()
currentpath = currentpath+'\DataSet'
for Table in TableNames:
    df = FatchData(Table)
    df.to_csv(currentpath+'/'f"{Table}.csv")
    print(f"Done for the Table: {Table}")

