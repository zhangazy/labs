import psycopg2
conn = psycopg2.connect("dbname=zhangazy user = postgres password=0000")
cur = conn.cursor()
cur.execute("UPDATE students set EMAIL ='updated@email.com' WHERE ID=1")
conn.commit()
print("Succesfully")
print("Total row affected:"+str(cur.rowcount))