import psycopg2
conn = psycopg2.connect("dbname = zhangazy user = postgres password = 0000")
cur = conn.cursor()
cur.execute("INSERT INTO students(ID, NAME, EMAIL, AGE) VALUES(1, 'Zhangazy', 'zhangazy@gmail.com', 18)")
conn.commit()
print("Successfully")
conn.close()
