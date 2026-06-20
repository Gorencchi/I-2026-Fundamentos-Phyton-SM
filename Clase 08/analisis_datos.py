import pandas
datos = pandas.read_csv("Clase 08/Estudiantes.csv")
print(datos)
print(datos.head())

#Estadisticas
print(datos.describe())

#Mostrar solo las columnas nombre y apellidos
print(datos[["nombre","apellido"]].head())

#calcular el maximo de la edad
print(datos['edad'].max)

#calcular el minimo de la edad
print(datos['edad'].min)

#filtrar estudiantes con calificacion mayor
estudiantes_alta_nota = datos[datos['nota']>85]
print(estudiantes_alta_nota)

#agrupar por género y calcular la media de las notas
media_por_genero = datos.groupby('sexo')['nota'].mean()
print(media_por_genero)