import psycopg2
conn = psycopg2.connect("dbname = zhangazy user = postgres password = 0000")
cur=conn.cursor()
cur.execute("""

CREATE TABLE Students(
ID INT NOT NULL,
NAME TEXT NOT NULL,
EMAIL TEXT NOT NULL,
AGE INT NOT NULL
)

""")
conn.commit()
print("Table created succesfully")