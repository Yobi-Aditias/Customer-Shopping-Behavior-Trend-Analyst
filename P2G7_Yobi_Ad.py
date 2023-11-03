'''
=================================================
Graded Challenge 7

Nama  : Yobi Aditias
Batch : FTDS-008-HCK

Program ini dibuat untuk melakukan automatisasi transform dan load data dari PostgreSQL ke ElasticSearch. Dataset yang dipakai adalah dataset mengenai penjualan mobil di Indonesia selama tahun 2020.
=================================================
'''
import pandas as pd
from sqlalchemy import create_engine
from elasticsearch import Elasticsearch

def Get_From_pg(host, database, table, username, password, port=5432):
# function ini digunakan untuk mengambil atau membaca data dari postgrese yang terdiri atas parameter nama host, database, tabel dan sebagainya untuk dipanggil melaui function create_engine
   conn_string = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
   conn = create_engine(conn_string)
   dataframe = pd.read_sql_query(f"SELECT * FROM {table}", conn)
   return dataframe

# data dari akun postgrese yang digunakan
host = 'localhost'
database = 'database_gc7'
table = 'table_gc7'
username = 'postgres'
password = 'Post'

data = Get_From_pg(host, database, table, username, password)
df = data.copy()
print(df.head())
print("\n")

def Cleaning(cleaning):
# function ini digunakan untuk cleaning data seperti handling missing value, mengubah nama kolom, dan sebagainya
    cleaning.dropna(inplace=True)
    cleaning.columns = cleaning.columns.str.lower().str.replace(' ', '_').str.replace('[\(\)]', '', regex=True)
    return cleaning

dfc = Cleaning(df)
print("cleaned data is in 'dfc'------\n'dfc' will be used for export to new csv and will be uploaded to Kibana----")
print(dfc.head())
print(" ")

# menyimpan data yang sudah clean menjadi file csv
dfc.to_csv("P2G7_Yobi_Ad_data_clean.csv", index=False)
print("Saving Complete to newest csv-------")

print("\nstart uploading")

def Upload_Elasticsearch(dataframe, index_name, es_url='http://localhost:9200'):
# Function ini digunakan untuk mengupload data dari csv yang sudah bersih
    es = Elasticsearch(es_url)

    for i, row in dataframe.iterrows():
        doc = row.to_json()
        es.index(index=index_name, id=i + 1, body=doc)
        if i % 500 == 0:
            print(f"{i} datas are complete")

    print('====== Finished Migrating Data ======')


Upload_Elasticsearch(dfc, index_name='gc7_customer_behaviour')
