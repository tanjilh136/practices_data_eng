import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database ="practice_db",
    user ="postgres",
    password = "1234"
)

cursor = conn.cursor()
print("Connectd")
# cursor.execute("Create Table Family( First_Name varchar (255)  Not Null , last_name varchar(255), contact varchar (255), age int,nationlaity varchar (255), relation varchar (255))")
# cursor.execute("Insert into Family values('Tanjil', 'Hasan','+351939962733',30,'Bangladeshi','Family Head')")
# cursor.execute("Insert into Family values('Nusrat', 'Jahan','+351920532714',24,'Bangladeshi','Wife')")
# cursor.execute("Insert into Family values('Iyaan', 'Hasan','+351939962733',0.6,'POrtugues','son')")
# conn.commit()
cursor.execute("Select * from Family")
print(*cursor.fetchall(),sep='\n')
cursor.close()
conn.close()