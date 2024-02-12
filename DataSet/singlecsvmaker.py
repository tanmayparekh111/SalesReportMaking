import pandas as pd

'''
List of your csv files
create one csv on which we are going to make visualization in power bi
in power bi we can get the rough idea in model page about the different data sheet  connections
you can do this authomatically too but every time you store new dataset into this folder i prefer to provide name manually
'''

FilesAvailableAtPath = ['businesses.csv', 'locations.csv', 'orders.csv', 'order_items.csv', 'products.csv', 'products_pricing_inventory.csv']

# Create a Pandas Excel writer using openpyxl as the engine.
writer = pd.ExcelWriter('FinalDataset.xlsx', engine='openpyxl')

# Write each csv file to a different worksheet.
for csv_file in FilesAvailableAtPath:
    try:
        df = pd.read_csv(csv_file)
        df.to_excel(writer, sheet_name=csv_file[:-4], index=False)
    except Exception as e:
        print(f"Error processing file {csv_file}: {e}")

# Close the Pandas Excel writer and output the Excel file.
writer.save()
