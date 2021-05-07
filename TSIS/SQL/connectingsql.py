import psycopg2
try:
    con = psycopg2.connect("dbname = zhangazy user = postgres password = 0000")
    print("Successfull!")
except:
    print("Unsuccesfully!!!!!!!!!!!")