# programa para que indique el precio de venta de un articulo dado.

#input
precio_costo = int(input("digite el valor del articulo dado: "))

#processing
if precio_costo < 3000:
    ganancia = precio_costo*0.15
    precio_venta = precio_costo + ganancia
else:
    if precio_costo > 6000:
        ganancia = 500
        precio_venta = precio_costo + ganancia
    else:
        ganancia = precio_costo*0.25
        precio_venta = precio_costo + ganancia

#output

print("el precio de venta es: " + str(precio_venta))
