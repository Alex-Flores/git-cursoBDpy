import mysql.connector
import pandas as pd
import os
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="prueba02"
    #port=""
)
conn.commit()


cursor=conn.cursor()
#cursor.execute("CREATE DATABASE prueba02")
#cursor.execute("CREATE TABLE usuario_nombres (nombre_personas VARCHAR(200))")
#bd_nombres=cursor.fetchall()
#print(bd_nombres)
#os.system ("cls")

#df = pd.read_excel("clase.xlsx",sheet_name="hoja1")
#print("Encabezado: ",df.columns)
#sql="""INSERT INTO nombres VALUES(%s)"""

lista_valor=int(input("Cuantos Alumnos quiere agregar a la bd"))
x=0
while x<lista_valor:
    sql="""INSERT INTO usuario_nombres VALUES(%s)"""
    val =str(input("Ingrese un valor para la bd: "))
    cursor.execute(sql, (val,))
    x+=1

cursor.execute("SELECT * FROM usuario_nombres")
x=cursor.fetchall()

#XLSX->DF->BD->DF->XLSX
lista_alumnos=[]
for datos in x:
    nombre_referencia=datos[0]
    lista_alumnos.append(nombre_referencia)
    print(nombre_referencia)
print(lista_alumnos)

#crear data frame o diccionario
dic_paises={"Lista de Alumnos": lista_alumnos}
df2=pd.DataFrame(dic_paises, columns=["alumnos que fueron integrados"])
#para escribir un excel
df2.to_excel(r'clase.xlsx', index=False, header=True)
print(df2)1
print("Inmprimo la lista: "x)
conn.close()