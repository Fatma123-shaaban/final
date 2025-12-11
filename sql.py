import sqlite3

connect=sqlite3.connect('fatma_DB.db')
cursor=connect.cursor()

#                             create tabels

cursor.execute("CREATE TABLE Medicine( MID INT PRIMARY KEY,Name TEXT(100),Price DECIMAL(8,2),Quantity INT,EndDate DATE)")
cursor.execute("CREATE TABLE Customer( CID INT PRIMARY KEY,Name TEXT(100),Phone TEXT(11),Address TEXT(150))")
cursor.execute("CREATE TABLE Doctor(DID INT PRIMARY KEY ,Name TEXT(100),Specialization TEXT(100),Phone TEXT(11))")
cursor.execute("CREATE TABLE Sale( SID INT PRIMARY KEY,Date DATE,CID INT  ,Total_amount DECIMAL(10,2),FOREIGN KEY (CID) REFERENCES Customer (CID) ON DELETE CASCADE)")



#                              insert values

m_row=[
    (1,'Panadol',75.50,100,'2025-12-05'),
    (2,'Amolix',85.75,80,'2025-12-12'),
    (3,'Panadol',100.00,100,'2026-12-05'),
    (4,'Panadol Extra',150.00,30,'2027-12-05'),
    (5,'Augmentin',95.50,100,'2028-12-05'),
    (6,'Cataflam',35.50,100,'2028-12-06'),
]
c_row=[
    (1,'Fatma Shaaban','01009457921','menofia'),
    (2,'Aya Shaaban','01234567891','menofia'),
    (3,'Mariam Shaaban','01006525921','menofia'),
    (4,'Manssa Shaaban','01116542391','menofia'),
    (5,'Safa Shaaban','01209457921','menofia'),
    (6,'Heba Nasser','01509457921','menofia')
]
d_row=[
    (1,'Amin','pediatrics','963287400'),
    (2,'Esraa','pediatrics','96387400'),
    (3,'Rawan','pediatrics','962587400'),
    (4,'Aya','pediatrics','9587400'),
    (5,'Reem','pediatrics','96327400'),
    (6,'Asmaa','pediatrics','9687400')
]
s_row=[
    (1,'2025-06-03',1,150.50),
    (2,'2024-06-03',2,50.50,),
    (3,'2022-06-03',3,170.50),
    (4,'2023-06-03',4,100.00),
    (5,'2021-06-03',5,80.50),
    (6,'2020-06-03',6,60.50),
]

connect.executemany("INSERT INTO Medicine VALUES(?,?,?,?,?)",m_row)
connect.executemany("INSERT INTO Customer VALUES(?,?,?,?)",c_row)
connect.executemany("INSERT INTO Doctor VALUES(?,?,?,?)",d_row)
connect.executemany("INSERT INTO Sale VALUES(?,?,?,?)",s_row)


#                      update

cursor.execute("UPDATE Customer SET Phone='123' WHERE CID=1")
cursor.execute("UPDATE Doctor SET Name='Ahmed' WHERE DID=1")
cursor.execute("UPDATE Sale SET Total_amount=60.00 WHERE SID=1")
cursor.execute("UPDATE Medicine SET Price=60.00, Name='Cital' WHERE MID=1")


#                         DELETING RECORDS

cursor.execute("DELETE FROM Medicine WHERE MID=5")
cursor.execute("UPDATE Medicine SET MID=MID-1 WHERE MID>5")

cursor.execute("SELECT CID FROM Customer WHERE Name='Manssa Shaaban'")
C=cursor.fetchone()
cursor.execute("DELETE FROM Customer WHERE Name='Manssa Shaaban'")
cursor.execute("UPDATE Customer SET CID=CID-1 WHERE CID>?",(C[0],))


cursor.execute("SELECT DID FROM Doctor WHERE Name='Ahmed'")
D=cursor.fetchone()
cursor.execute("DELETE FROM Doctor WHERE Name='Ahmed'")
cursor.execute("UPDATE Doctor SET DID=DID-1 WHERE DID>?",(D[0],))

cursor.execute("SELECT SID FROM Sale WHERE Total_amount=60.00")
S=cursor.fetchone()
cursor.execute("DELETE FROM Sale WHERE Total_amount=60.00")
cursor.execute("UPDATE Sale SET SID=SID-1,CID=CID-1 WHERE SID>?",(S[0],))




#                         Searching

S_M=input("Enter Medicine ID or Name to search: ")
if S_M.isdigit():
    cursor.execute("SELECT * FROM Medicine WHERE MID=?",(int(S_M),))
else:
    cursor.execute("SELECT * FROM Medicine WHERE Name LIKE ?",('%'+S_M+'%'),)
result_M=cursor.fetchall()
if result_M:
    for row in result_M:
        print(row)
else:
    print("No result found.")

S_D=input("Enter Doctor ID or Name to search: ")
if S_D.isdigit():
    cursor.execute("SELECT * FROM Doctor WHERE DID=?",(int(S_D),))
else:
    cursor.execute("SELECT * FROM Doctor WHERE Name LIKE ?",('%'+S_D+'%',))
result_D=cursor.fetchall()
if result_D:
    for row in result_D:
        print(row)
else:
    print("No result found.")


S_C=input("Enter Customer ID or Name to search: ")
if S_C.isdigit():
    cursor.execute("SELECT * FROM Customer WHERE CID=?",(int(S_C),))
else:
    cursor.execute("SELECT * FROM Customer WHERE Name LIKE ?",('%'+S_C+'%'),)
result_C=cursor.fetchall()
if result_C:
    for row in result_C:
        print(row)
else:
    print("No result found.")


S_S=input("Enter Sale ID to search: ")
cursor.execute("SELECT * FROM Sale WHERE SID=?",(int(S_S),))
result_S=cursor.fetchall()
if result_S:
    for row in result_S:
        print(row)
else:
    print("No result found.")



connect.commit()
connect.close()