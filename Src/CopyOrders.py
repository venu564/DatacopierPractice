BASE_DIR = 'D:\\DE\Material\\data-engineering-spark-main\\data-engineering-spark-main\\data\\retail_db_json'
table_name = 'orders'

import os
file_name = os.listdir(f'{BASE_DIR}\\{table_name}')[0]
fp = f'{BASE_DIR}\\{table_name}\\{file_name}'

import pandas as pd
json_reader = pd.read_json(fp, lines=True)

conn = 'postgresql://itversity_retail_user:itversity@localhost:5432/itversity_retail_db'

json_reader.to_sql(table_name, conn, if_exists='append', index=False)


#from sqlalchemy import create_engine
#conn = create_engine('mssql+pyodbc://retail_user:itversity@localhost:1433/itversity_retail_db?driver=SQL Server')

#file_reader = pd.read_json(fp, lines=True, chunksize=1000)
#for df in file_reader:
 #   min_key = df['order_id'].min()
  #  max_key = df['order_id'].max()
   # df.to_sql(table_name,conn,if_exists='append',index=False)
    #print(f'Processed SQL {table_name} within the range of {min_key} and {max_key}')

