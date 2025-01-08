import pandas as pd
import os
import time


df=pd.read_csv("/home/iabd/Escritorio/IA y BD/Big Data/BD Aplicado/UD2/2018.csv",nrows=10000)
start_time = time.time()
df.to_parquet("2018.parquet")
end_time = time.time()
elapsed_time = end_time - start_time
file_size = os.path.getsize("/home/iabd/Escritorio/IA y BD/2018.parquet")
print(f"Tiempo de creación del archivo Parquet: {elapsed_time:.2f} segundos")
print(f"Tamaño del archivo Parquet: {file_size / (1024 * 1024):.2f} MB")

#df=pd.read_parquet("/home/iabd/Escritorio/IA y BD/2018.parquet")
#print(df.head())