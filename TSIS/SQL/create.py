import psycopg2

con = psycopg2.connect(database = 'postgres', user ='postgres',password ='0000',host ='127.0.0.1',port='5432')
con.autocommit=True
cursor = con.cursor()
sql='''Create database Zhangazy ''';
cursor.execute(sql)
print('database created succesfully')
con.close()