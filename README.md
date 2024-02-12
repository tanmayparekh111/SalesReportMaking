# SalesReportMaking
This is the coding portion and report is generated in powerbi

*****************************************************************************************************************
PYTHON CLEANING AND DATA PREPARING PART
*****************************************************************************************************************
here i have 1project folder named DATAANALYSISINTERVIEW
in which i have made 3python files
1 is GetData.py
this file contains the functions to fatch the data from the database and store it in csv for look at the data spread

2Conversion.py
where we are getting the functions from GetData.py, and all the available data is stored in csv in a folder named DataSet

3)crosssellingdataframe.py
this file is use to generate the cross selling product top most product that is sold with each unique product, and this is based on user_id that have purchased.

in the DataSet folder you will find another python file named
1) singlecsvmaker.py
this file is used to make single csv that contains all the available(6) tables in to one csv but in the different sheet

*******************************************************************
Table visualization part
*******************************************************************

in tablue i have loaded two dataset of csv named finalcsv which contains 6 tables in each sheet,
and another named relationship.csv which contains the inside of the product that are sold in pairs most by user_id orders.

after loading this two csv, i have seen the which is relation is available in between them and then, i perform the visualization in them.

this dashboard you can see at this link
https://app.powerbi.com/view?r=eyJrIjoiZjZmMmU5ZjgtMDA0Yy00ZjZmLTg1YTYtMzRmZDRlMWMyNzMyIiwidCI6IjkwODI1ZGI3LTBiOTYtNDNiYi05NjRhLWMxZjc2Nzg0Yjk2YSJ9
