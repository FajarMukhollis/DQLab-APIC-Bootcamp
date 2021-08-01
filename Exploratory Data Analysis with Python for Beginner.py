#https://academy.dqlab.id/main/livecode/163/308/1418?pr=0
#Memanggil library di Python
import numpy as np
import pandas as pd

#https://academy.dqlab.id/main/livecode/163/309/1420?pr=0
#Tugas Praktek
import pandas as pd
order_df = pd.read_csv("order.csv")

#https://academy.dqlab.id/main/livecode/163/309/1423?pr=0
#Tugas Praktek
import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
print(order_df.shape)

#https://academy.dqlab.id/main/livecode/163/309/1425?pr=0
#Tugas Praktek
import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
print(order_df.head())

#https://academy.dqlab.id/main/livecode/163/309/1430?pr=0
#Tugas Praktek
import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
# Quick summary  dari segi kuantitas, harga, freight value, dan weight
print(order_df.describe())
# Median median dari total pembelian konsumen per transaksi kolom price
print(order_df.loc[:, "price"].median())

#https://academy.dqlab.id/main/livecode/163/310/1432?pr=0
#Tugas Praktek
import pandas as pd
import matplotlib.pyplot as plt
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
# plot histogram kolom: price
order_df[["price"]].hist(figsize=(4, 5), bins=10, xlabelsize=8, ylabelsize=8)
plt.show()  # Untuk menampilkan histogram plot

#https://academy.dqlab.id/main/livecode/163/310/1434?pr=0
#Tugas Praktek
import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
# Standar variasi kolom product_weight_gram
order_df.loc[:, "product_weight_gram"].std()
# Varians kolom product_weight_gram
order_df.loc[:, "product_weight_gram"].var()

#https://academy.dqlab.id/main/livecode/163/310/1436?pr=0
#Tugas Praktek
import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
# Hitung quartile 1
Q1 = order_df[["product_weight_gram"]].quantile(0.25)
# Hitung quartile 3
Q3 = order_df[["product_weight_gram"]].quantile(0.75)
# Hitung inter quartile range dan cetak ke console
IQR = Q3 - Q1
print(IQR)

#https://academy.dqlab.id/main/livecode/163/310/1438?pr=0
#Tugas Praktek
import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
# Ganti nama kolom freight_value menjadi shipping_cost
order_df.rename(columns={"freight_value": "shipping_cost"}, inplace=True)
print(order_df)

#https://academy.dqlab.id/main/livecode/163/310/1440?pr=0
#Tugas Praktek
import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
# Hitung rata rata dari price per payment_type
rata_rata = order_df["price"].groupby(order_df["payment_type"]).mean()
print(rata_rata)

#https://academy.dqlab.id/main/livecode/163/310/1442?pr=0
#Tugas Praktek
import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
# Hitung harga maksimum pembelian customer
sort_harga = order_df.sort_values(by="price", ascending=False)
print(sort_harga)
