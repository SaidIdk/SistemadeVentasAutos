from cliente import Cliente
from auto import Auto
from venta_detalle import VentaDetalle
from venta import Venta
""" crear un CRUD de persona"""
datos_inicial:list=[{"dni":"74205582",
                     "nombres":"Rossel Teofilo",
                     "apellidos":"Turpo Maza",
                     "direccion":"Jr. Pierola 264",
                     "telefono":"918112204",
                     },
                     {"dni":"73892328",
                     "nombres":"Howard Lemuel",
                     "apellidos":"Coila Alberto",
                     "direccion":"Slda. Arequipa km. 6",
                     "telefono":"912455789",
                     },
                     {"dni":"63536022",
                     "nombres":"Jean Carlos",
                     "apellidos":"Zela Pariapaza",
                     "direccion":"Santigo Rios",
                     "telefono":"928857886",
                     }]
                     
lista_clientes:Cliente=[]


def cargar_clientes():
    for dato in datos_inicial:
        lista_clientes.append(Cliente(len(lista_clientes),
                                dato["dni"],
                                dato["nombres"],
                                dato["apellidos"],
                                dato["direccion"],
                                dato["telefono"]))
    return lista_clientes
def insertar_cliente():
    dni:str = input("Ingrese el DNI del cliente: ")
    nombres:str = input("ingrese el nombre del cliente: ")
    apellidos:str = input("ingrese apellidos del cliente: ")
    direccion:str = input("ingrese la direccion del cliente: ")
    telefono:str = input("ingrese el telefono del cliente: ")
    lista_clientes.append(Cliente(len(lista_clientes)+1,dni,nombres,apellidos,direccion,telefono))
    return lista_clientes

def listar_clientes():
    print("======================LISTA DE CLIENTES=========================")
    print("================================================================")
    print("|ID|  DNI   |   NOMBRES  |  APELLIDOS  |  DIRECCION | TELEFONO|")
    print("================================================================")
    for client in lista_clientes:
        print("_______________________________________________________________")
        print(client.convertir_a_string())
        print("_______________________________________________________________")

def bucar_cliente():
    dni:str = input("Ingrese el DNI del cliente: ")
    for cliente in lista_clientes:
        if cliente.dni == dni:
            print(cliente.convertir_a_string())
            return cliente

def editar_cliente():
    listar_clientes()
    dni:str = input("ingrese el Dni del cliente: ")
    for cliente in lista_clientes:
        if cliente.dni == dni:
            print(cliente.convertir_a_string())
            cliente.dni = input("Ingrese DNI del cliente: ")
            cliente.nombres = input("Ingrese nombre del cliente: ")
            cliente.apellidos = input("ingrese  apellidos del cliente: ")
            cliente.direccion = input("ingrese direccion del cliente: ")
            cliente.telefono = input("ingrese el telefono del cliente: ")
    listar_clientes()

def eliminar_cliente():
    listar_clientes()
    dni:str = input("ingrese el dni del cliente: ")
    for index, cliente in enumerate(lista_clientes):
        if cliente.dni == dni:
            lista_clientes.pop(index)
    listar_clientes()



""" crear un CRUD de auto"""
datos_inicial_autos:list=[{"placa":"A7R-745",
                            "marca":"Chevrolet",
                            "modelo":"Onix Sedan Turbo",
                            "precio":54.632},
                            {"placa":"ACD-4AR",
                            "marca":"Chevrolet",
                            "modelo":"Camaro",
                            "precio":230.962},
                            {"placa":"4AR-AR8",
                            "marca":"Chevrolet",
                            "modelo":"Tracker Turbo",
                            "precio":78.887}]
lista_autos:Auto=[]


def cargar_autos():
    for dato in datos_inicial_autos:
        lista_autos.append(Auto(
                                dato["placa"],
                                dato["marca"],
                                dato["modelo"],
                                dato["precio"]))
    return lista_autos
def insertar_auto():
    placa:str = input("Ingrese la placa del auto: ")
    marca:str = input("ingrese la marca del auto: ")
    modelo:str = input("ingrese el modelo del auto: ")
    precio:float = float(input("ingrese el precio del auto: "))
    
    lista_autos.append(Auto(placa,marca,modelo,precio))
    return lista_autos

def listar_autos():
    print("======================LISTA DE AUTOS=========================")
    print("================================================================")
    print("|PLACA|  MARCA   |  MODELO  |  PRECIO  |")
    print("================================================================")
    for auto in lista_autos:
        print("_______________________________________________________________")
        print(auto.convertir_a_string())
        print("_______________________________________________________________")

def bucar_auto():
    placa:str = input("Ingrese la placa del auto: ")
    for auto in lista_autos:
        if auto.placa == placa:
            print(auto.convertir_a_string())
            return auto

def editar_auto():
    listar_autos()
    placa:str = input("ingrese la placa del auto: ")
    for auto in lista_autos:
        if auto.placa == placa:
            print(auto.convertir_a_string())
            auto.marca = input("Ingrese la marca del auto: ")
            auto.modelo = input("Ingrese el modelo del auto: ")
            auto.precio = input("ingrese el precio del auto: ")
            
    listar_autos()

def eliminar_auto():
    listar_autos()
    placa:str = input("ingrese placa del auto: ")
    for index, auto in enumerate(lista_autos):
        if auto.placa == placa:
            lista_autos.pop(index)
    listar_autos()
    return lista_autos
venta_detalles:VentaDetalle=[]

def agregar_autos():
    auto:Auto=bucar_auto()
    cantidad:float=float(input("Ingrese la cantidad: "))
    venta_detalles.append(VentaDetalle(len(venta_detalles)+1,auto.placa,auto.marca,cantidad,auto.precio))
    return venta_detalles
ventas:Venta=[]
def insertar_venta():
    cliente:Cliente=bucar_cliente()
    continuar_agregando_auto:bool=True
    while continuar_agregando_auto:
        opcion:str=input("1 para agregar auto, 2 para guardar venta: ")
        match opcion:
            case "1":
                agregar_autos()
            case "2":
                continuar_agregando_auto=False
    total_venta:float=0
    for venta_detalle in venta_detalles:
        print(venta_detalle.convertir_a_string())
        total_venta=total_venta+venta_detalle.total
    venta:Venta=Venta(len(ventas)+1,cliente,venta_detalles,total_venta)
    ventas.append(venta)
    return ventas
def listar_ventas():
    for venta in ventas:
        print(venta.convertir_a_string())
    return ventas

def buscar_venta():
    numero:int=int(input("Ingrese el numero de la venta: "))
    for venta in ventas:
        if venta.numero==numero:
            print(venta.convertir_a_string())
            for detalle in venta.detalle:
                print(detalle.convertir_a_string())
            return venta


def menu_texto():
    print("=============MENU============")
    print("=========CRUD CLIENTE========")
    print("OPCION 1 PARA CREAR CLIENTE")
    print("OPCION 2 PARA LISTAR")
    print("OPCION 3 PARA BUSCAR CLIENTE")
    print("OPCION 4 PARA EDITAR CLIENTE")
    print("OPCION 5 PARA ELIMINAR CLIENTE")
    print("=========CRUD AUTO========")
    print("OPCION 6 PARA CREAR AUTO")
    print("OPCION 7 PARA LISTAR AUTO")
    print("OPCION 8 PARA BUSCAR AUTO")
    print("OPCION 9 PARA EDITAR AUTO")
    print("OPCION 10 PARA ELIMINAR AUTO")
    print("=========CRUD VENTA========")
    print("OPCION 11 PARA REGISTRAR VENTA")
    print("OPCION 12 PARA LISTAR VENTA")
    print("OPCION 13 PARA BUSCAR VENTA")
    print("OPCION 14 PARA SALIR")

def menu():
    continuar:bool=True
    while continuar:
        menu_texto()  
        opcion:str
        opcion = input("Ingrese la opcion: ")
        match opcion:
            case "1":
                insertar_cliente()
            case "2": 
                listar_clientes()
            case "3":
                bucar_cliente()
            case "4":
                editar_cliente()
            case "5":
                eliminar_cliente()
            case "6":
                insertar_auto()
            case "7": 
                listar_autos()
            case "8":
                bucar_auto()
            case "9":
                editar_auto()
            case "10":
                eliminar_auto()
            case "11":
                insertar_venta()
            case "12":
                listar_ventas()
            case "13":
                buscar_venta()
            case "14":
                print("Saliendo del programa")
                continuar = False

def main():
    cargar_clientes()
    cargar_autos()
    menu()    
    print("Iniciando programa")
    return True

if __name__== '__main__':
    main()
