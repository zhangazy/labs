import psycopg2
conn = psycopg2.connect("dbname = zhangazy user = postgres password= 0000")
cur = conn.cursor()
cur.execute("SELECT ID, NAME, EMAIL, AGE FROM students")
rows = cur.fetchall()
for data in rows:
    print("ID:" +str(data[0]))
    print("NAME:"+ data[1])
    print("EMAIL"+ data[2])
    print("AGE:" + str(data[3]))
print("Succesfully") 