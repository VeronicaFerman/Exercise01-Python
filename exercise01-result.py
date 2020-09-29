listaRegistros = []
listaSuma = []
clientes=1

while clientes>0:
    cliente = input("nombre del cliente: ")
    producto = input("producto: ")
    cost = float(input("Costo del producto: "))

    soloCosto = dict(costo=cost)
    listaSuma.append(soloCosto["costo"])
    registro = dict(cliente=cliente, producto=producto, costo=cost)
    listaRegistros.append(registro)

    pregunta = input("¿Desea registrar otro cliente? (Si/No) ")

    if pregunta.lower() == "si":
        clientes+=1
    else:
        clientes=0

suma = 0
for soloCosto in listaSuma:
    suma = suma + soloCosto
print("El costo total en $ hasta el momento es:")
print(suma)

detalle = input("¿Desea ver el detalle de todos los clientes registrados? (Si/No) ")
if detalle.lower() == "si":
    for registro in listaRegistros:
        print(registro)
    print("Tenga un buen día")
else:
    print("Tenga un buen día")