-- Buat database
CREATE DATABASE database_gc7;


-- Buat tabel
CREATE TABLE table_gc7(
"Customer ID" INTEGER,
"Age" INTEGER,
"Gender" VARCHAR(100),
"Item Purchased" VARCHAR(100),
"Category" VARCHAR(100),
"Purchase Amount (USD)" INTEGER,
"Location" VARCHAR(100), 
"Size" VARCHAR(100), 
"Color" VARCHAR(100), 
"Season" VARCHAR(100),
"Review Rating" NUMERIC(2), 
"Subscription Status" VARCHAR(100), 
"Shipping Type" VARCHAR(100),
"Discount Applied" VARCHAR(100),
"Promo Code Used" VARCHAR(100),
"Previous Purchases" INTEGER,
"Payment Method" VARCHAR(100),
"Frequency of Purchases" VARCHAR(100)
);

-- Import data dari file CSV
COPY table_gc7
FROM 'C:\BootcampHacktiv8\Graded Challange\GC7\p2-ftds008-hck-g7-Yobi-Aditias\P2G7_Yobi_Ad_data_raw.csv'
DELIMITER ','
CSV HEADER;

SELECT * FROM table_gc7;


/*
Kode diatas merupakan hasil download dari kodingan di Postgres
Kode tersebut di run bagian create database secara terpisah dengan baris kode setelahnya
Pembuatan nama kolom disamakan dengan nama kolom pada tabel data raw di csv
*/