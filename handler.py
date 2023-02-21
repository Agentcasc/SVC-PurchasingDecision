
import pymysql

endpoint = 'mwsmaster-dtc-r.cfx5gks3rioa.us-east-1.rds.amazonaws.com'
username = 'yanjie_zheng'
password = '4pGp37bvNnjHEejb'
database_name = '*'


connection = pymysql.connect(host=endpoint, user=username, passwd=password, db=database_name, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version : %s " % data)
#%%
