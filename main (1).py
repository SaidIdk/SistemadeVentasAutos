from tkinter import Tk, Label, Entry, Button, Scrollbar, Listbox, StringVar, messagebox
from cliente import Cliente
from auto import Auto
from venta_detalle import VentaDetalle
from venta import Venta

datos_inicial = [
    {"dni": "74205582",
     "nombres": "Rossel Teofilo",
     "apellidos": "Turpo Maza",
     "direccion": "Jr Pierola",
     "telefono": "918112204"},

    {"dni": "76536017",
     "nombres": "Jean Carlos",
     "apellidos": "Zela Pariapaza",
     "direccion": "Santiago Rios",
     "telefono": "928857886"},

    {"dni": "76536022",
     "nombres": "Michael Alfredo",
     "apellidos": "Zela Pariapaza",
     "direccion": "Santiago Rios",
     "telefono": "978451234"},

    {"dni":"73892328",
     "nombres":"Howard Lemuel",
     "apellidos":"Coila Alberto",
     "direccion":"Slda Arequipa km6",
     "telefono":"956799529"
     }
]

lista_clientes = []

def cargar_clientes():
    for dato in datos_inicial:
        lista_clientes.append(Cliente(len(lista_clientes)+1, dato["dni"], dato["nombres"], dato["apellidos"], dato["direccion"], dato["telefono"]))
    return lista_clientes

def insertar_cliente():
    dni = entry_dni.get()
    nombres = entry_nombres.get()
    apellidos = entry_apellidos.get()
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()

    if not dni or not nombres or not apellidos or not direccion or not telefono:
        messagebox.showwarning("Campos Vacíos", "Por favor, complete todos los campos.")
        return

    lista_clientes.append(Cliente(len(lista_clientes) + 1, dni, nombres, apellidos, direccion, telefono))

    listar_cliente()

    entry_dni.delete(0, "end")
    entry_nombres.delete(0, "end")
    entry_apellidos.delete(0, "end")
    entry_direccion.delete(0, "end")
    entry_telefono.delete(0, "end")

def listar_cliente():
    listbox_clientes.delete(0, "end")
    listbox_clientes.insert("end", "|Nom")
    for client in lista_clientes:
        listbox_clientes.insert("end", client.convertir_a_string())

def buscar_cliente():
    dni = entry_dni.get()

    if not dni:
        messagebox.showwarning("Campo Vacío", "Por favor, ingrese el DNI de la cliente.")
        return

    for cliente in lista_clientes:
        if cliente.dni == dni:
            messagebox.showinfo("Cliente Encontrada", cliente.convertir_a_string())
            return cliente

    messagebox.showinfo("Cliente no encontrada", f"No se encontró ningun cliente con DNI: {dni}")

def editar_cliente():
    dni = entry_dni.get()

    if not dni:
        messagebox.showwarning("Campo Vacío", "Por favor, ingrese el DNI del cliente.")
        return

    for cliente in lista_clientes:
        if cliente.dni == dni:
            cliente.dni = entry_dni.get()
            cliente.nombres = entry_nombres.get()
            cliente.apellidos = entry_apellidos.get()
            cliente.direccion = entry_direccion.get()
            cliente.telefono = entry_telefono.get()

    listar_cliente()

    entry_dni.delete(0, "end")
    entry_nombres.delete(0, "end")
    entry_apellidos.delete(0, "end")
    entry_direccion.delete(0, "end")
    entry_telefono.delete(0, "end")

def eliminar_cliente():
    dni = entry_dni.get()

    if not dni:
        messagebox.showwarning("Campo Vacío", "Por favor, ingrese el DNI del cliente.")
        return

    for index, cliente in enumerate(lista_clientes):
        if cliente.dni == dni:
            lista_clientes.pop(index)

    listar_cliente()

    entry_dni.delete(0, "end")
    entry_nombres.delete(0, "end")
    entry_apellidos.delete(0, "end")
    entry_direccion.delete(0, "end")
    entry_telefono.delete(0, "end")

datos_inicial_autos = [   
     {"placa": "A7R-745",
    "marca": "Chevrolet",
     "precio": 54.632},
    {"placa": "ACD-4AR",
     "marca": "Chevrolet",
     "precio": 230.932},
    {"placa": "4AR-AR8",
     "marca": "Chevrolet",

     "precio": 78.887}]

lista_autos = []

def cargar_autos():
    for dato in datos_inicial_autos:
        lista_autos.append(Auto(dato["placa"], dato["marca"], dato["precio"]))
    return lista_autos

def insertar_auto():
    placa = entry_placa.get()
    marca = entry_nombre_auto.get()
    precio = entry_precio.get()

    if not placa or not marca or not precio:
        messagebox.showwarning("Campos Vacíos", "Por favor, complete todos los campos.")
        return

    lista_autos.append(Auto(placa, marca, precio))
    listar_autos()

    entry_placa.delete(0, "end")
    entry_nombre_auto.delete(0, "end")
    entry_precio.delete(0, "end")

def listar_autos():
    listbox_autos.delete(0, "end")
    for auto in lista_autos:
        listbox_autos.insert("end", auto.convertir_a_string())

def buscar_auto():
    placa = entry_placa.get()

    if not placa:
        messagebox.showwarning("Campo Vacío", "Por favor, ingrese la placa del auto.")
        return

    for auto in lista_autos:
        if auto.placa == placa:
            messagebox.showinfo("Auto Encontrado", placa.convertir_a_string())
            return placa

    messagebox.showinfo("Auto no encontrado", f"No se encontró ningún auto con placa: {placa}")

def editar_auto():
    placa = entry_placa.get()

    if not placa:
        messagebox.showwarning("Campo Vacío", "Por favor, ingrese la placa del auto.")
        return

    for auto in lista_autos:
        if auto.placa == placa:
            auto.placa = entry_placa.get()
            auto.nombre = entry_nombre_auto.get()
            auto.precio = entry_precio.get()

    listar_autos()

    entry_placa.delete(0, "end")
    entry_nombre_auto.delete(0, "end")
    entry_precio.delete(0, "end")

def eliminar_auto():
    placa = entry_placa.get()

    if not placa:
        messagebox.showwarning("Campo Vacío", "Por favor, ingrese la placa del auto.")
        return

    for index, producto in enumerate(lista_autos):
        if producto.placa == placa:
            lista_autos.pop(index)

    listar_autos()

    entry_placa.delete(0, "end")
    entry_nombre_auto.delete(0, "end")
    entry_precio.delete(0, "end")

def realizar_venta():
    cliente = buscar_cliente()
    if cliente is None:
        return

    listado_autos = []
    total = 0

    while True:
        placa = entry_placa.get()

        if not placa:
            break

        auto = buscar_auto()
        if auto is not None:
            cantidad = int(entry_cantidad.get())
            precio_unitario = float(auto.precio)
            total_auto = cantidad * precio_unitario

            venta_detalle = VentaDetalle(len(listado_autos) + 1, placa, auto.nombre, cantidad, precio_unitario)
            listado_autos.append(venta_detalle)
            total += total_auto

        entry_placa.delete(0, "end")
        entry_cantidad.delete(0, "end")

    if not listado_autos:
        messagebox.showwarning("Autos Vacíos", "Por favor, ingrese al menos un auto para realizar la venta.")
        return

# Cargar datos iniciales
cargar_clientes()
cargar_autos()

# Crear ventana principal
window = Tk()
window.title("Sistema de Ventas")

# Etiquetas y campos de texto para el módulo de Personas
label_dni = Label(window, text="DNI:")
label_dni.grid(row=0, column=0, padx=10, pady=5)
entry_dni = Entry(window)
entry_dni.grid(row=0, column=1, padx=10, pady=5)

label_nombres = Label(window, text="Nombres:")
label_nombres.grid(row=1, column=0, padx=10, pady=5)
entry_nombres = Entry(window)
entry_nombres.grid(row=1, column=1, padx=10, pady=5)

label_apellidos = Label(window, text="Apellidos:")
label_apellidos.grid(row=2, column=0, padx=10, pady=5)
entry_apellidos = Entry(window)
entry_apellidos.grid(row=2, column=1, padx=10, pady=5)

label_direccion = Label(window, text="Dirección:")
label_direccion.grid(row=3, column=0, padx=10, pady=5)
entry_direccion = Entry(window)
entry_direccion.grid(row=3, column=1, padx=10, pady=5)

label_telefono = Label(window, text="Teléfono:")
label_telefono.grid(row=4, column=0, padx=10, pady=5)
entry_telefono = Entry(window)
entry_telefono.grid(row=4, column=1, padx=10, pady=5)

button_insertar_cliente = Button(window, text="Insertar", command=insertar_cliente)
button_insertar_cliente.grid(row=5, column=0, padx=10, pady=5)

button_listar_clientes = Button(window, text="Listar", command=listar_cliente)
button_listar_clientes.grid(row=5, column=1, padx=10, pady=5)

button_buscar_cliente = Button(window, text="Buscar", command=buscar_cliente)
button_buscar_cliente.grid(row=5, column=2, padx=10, pady=5)

button_editar_cliente = Button(window, text="Editar", command=editar_cliente)
button_editar_cliente.grid(row=5, column=3, padx=10, pady=5)

button_eliminar_cliente = Button(window, text="Eliminar", command=eliminar_cliente)
button_eliminar_cliente.grid(row=5, column=4, padx=10, pady=5)

# Etiquetas y campos de texto para el módulo de Productos
label_placa = Label(window, text="Placa:")
label_placa.grid(row=6, column=0, padx=10, pady=5)
entry_placa = Entry(window)
entry_placa.grid(row=6, column=1, padx=10, pady=5)

label_nombre_auto = Label(window, text="Nombre:")
label_nombre_auto.grid(row=7, column=0, padx=10, pady=5)
entry_nombre_auto = Entry(window)
entry_nombre_auto.grid(row=7, column=1, padx=10, pady=5)

label_precio = Label(window, text="Precio:")
label_precio.grid(row=8, column=0, padx=10, pady=5)
entry_precio = Entry(window)
entry_precio.grid(row=8, column=1, padx=10, pady=5)

button_insertar_auto = Button(window, text="Insertar", command=insertar_auto)
button_insertar_auto.grid(row=9, column=0, padx=10, pady=5)

button_listar_autos = Button(window, text="Listar", command=listar_autos)
button_listar_autos.grid(row=9, column=1, padx=10, pady=5)

button_buscar_auto = Button(window, text="Buscar", command=buscar_auto)
button_buscar_auto.grid(row=9, column=2, padx=10, pady=5)

button_editar_auto = Button(window, text="Editar", command=editar_auto)
button_editar_auto.grid(row=9, column=3, padx=10, pady=5)

button_eliminar_auto = Button(window, text="Eliminar", command=eliminar_auto)
button_eliminar_auto.grid(row=9, column=4, padx=10, pady=5)

# Etiquetas y campos de texto para el módulo de Ventas
label_placa_auto = Label(window, text="Placa del Auto:")
label_placa_auto.grid(row=10, column=0, padx=10, pady=5)
entry_placa = Entry(window)
entry_placa.grid(row=10, column=1, padx=10, pady=5)

label_cantidad = Label(window, text="Cantidad:")
label_cantidad.grid(row=10, column=2, padx=10, pady=5)
entry_cantidad = Entry(window)
entry_cantidad.grid(row=10, column=3, padx=10, pady=5)

button_realizar_venta = Button(window, text="Realizar Venta", command=realizar_venta)
button_realizar_venta.grid(row=10, column=4, padx=10, pady=5)

# Listbox para mostrar los resultados
listbox_clientes = Listbox(window, width=80)
listbox_clientes.grid(row=11, column=0, columnspan=5, padx=10, pady=5)

listbox_autos = Listbox(window, width=80)
listbox_autos.grid(row=12, column=0, columnspan=5, padx=10, pady=5)

listbox_ventas = Listbox(window, width=80)
listbox_ventas.grid(row=13, column=0, columnspan=5, padx=10, pady=5)

# Scrollbar para los Listbox
scrollbar_clientes = Scrollbar(window)
scrollbar_clientes.grid(row=11, column=5, sticky="ns")
listbox_clientes.config(yscrollcommand=scrollbar_clientes.set)
scrollbar_clientes.config(command=listbox_clientes.yview)

scrollbar_autos = Scrollbar(window)
scrollbar_autos.grid(row=12, column=5, sticky="ns")
listbox_autos.config(yscrollcommand=scrollbar_autos.set)
scrollbar_autos.config(command=listbox_autos.yview)

scrollbar_ventas = Scrollbar(window)
scrollbar_ventas.grid(row=13, column=5, sticky="ns")
listbox_ventas.config(yscrollcommand=scrollbar_ventas.set)
scrollbar_ventas.config(command=listbox_ventas.yview)

# Ejecutar ventana
window.mainloop()