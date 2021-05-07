import psycopg2
conn = psycopg2.connect("dbname=zhangazy user= postgres password= 0000")
cur = conn.cursor()
cur.execute("DELETE FROM students WHERE ID = 1")
conn.commit()
print("DATA DELETED")
print("Total row affected: " + str(cur.rowcount))