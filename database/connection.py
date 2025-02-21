import pymysql
import pandas as pd 

csv = "data\candidates.csv"
df = pd.read_csv(csv)


def connection ():
    try:
        connection= pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='workshop_1'
            )
        if connection:
            print("conexion exitosa con la base de datos")
            return connection
    except pymysql.MySQLError as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None
    
    
if __name__ == '__main__':
    connection = connection()
    if connection:
        print(df.head)
        print(df.describe)
        print(df.info)
    else:
        print("No se pudo establecer la conexión a la base de datos")