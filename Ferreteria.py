#programa ferretria
nombre = ""
tipocable = ""
cantidadmetro = 0
montoAbonar = 0.0
totalAPagar = 0.0
descuento = 0.0

nombre = input("Ingrese el nombre del cliente: ")
tipocable = input("Elija el tipo de cable que desea comprar [Gold o Silver]?: ")
cantidadmetro = int(input("Ingrese la canitdad de metro de cable que desea comprar: "))

if tipocable == "gold":
    montoAbonar = cantidadmetro * 6000
       
elif tipocable == "silver":
    montoAbonar = cantidadmetro * 4000
      
if cantidadmetro >= 100:
    descuento = montoAbonar * 0.17
else:
    pass
    
totalAPagar = montoAbonar - descuento # SE APLICA UN DESCUENTO SI ES QUE EL CLIENTE COMPRO MAS DE 100 METROS DE CABLE

print("---Factura del cliente--- ")
print("Nombre del cliente:",nombre)
print("Tipo de cable adquirido: ",tipocable)
print("Monto total a pagar es de: Gs.", totalAPagar)
print("Descuento: ",descuento)
  
    
    
    
    
    
