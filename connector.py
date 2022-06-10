import mysql.connector 

def conn():
    mydb = mysql.connector.connect(
        host="localhost",
        user="thunder",
        password="",
        database="hardware"
    )
    return mydb

class Get:
    
    def update_hw(self, Id, status, value):
        mydb = conn()
        cs = mydb.cursor()
        sql = f"UPDATE hardware_control SET status='{status}', value={value} WHERE id={Id}" 
        cs.execute(sql)
        mydb.commit()
        cs.close()
        mydb.close()
        
        return True
    
class Post:
    
    def update_post(self, Id, name, Type):
        mydb = conn()
        cs = mydb.cursor()
        sql = f"UPDATE hardware_control SET name='{name}', type='{Type}' WHERE id={Id}"
        cs.execute(sql)
        mydb.commit()
        cs.close()
        mydb.close()
        return True
