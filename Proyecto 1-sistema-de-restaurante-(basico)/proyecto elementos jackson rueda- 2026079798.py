"""
curso: Elementos de Computación T.E.C
Proyecto I
Semestre I
Estudiante: JACKSON RUEDA BOLAÑOS
Carné: 2026079798
Fecha de entrega: 20 de abril
fecha revision: 20 de abril
"""





#creacion del diccionario con algunos elementos basicos
                 #tipos de arroz en el menu por stock
productos = {9:{"nom":"Arroz tipico","tipo":"Plato fuerte","precio":2450,"cantidad":40},
             ----------------------------------------------------------------------------
             10:{"nom":"Arroz blanco","tipo":"Plato fuerte","precio":2000,"cantidad":40},   
             --------------------------------------------------------------------------------
             11:{"nom":"Arroz con pollo","tipo":"Plato fuerte","precio":4000,"cantidad":30},
             --------------------------------------------------------------------------------
             12:{"nom":"Arroz cantones","tipo":"Plato fuerte","precio": 5500,"cantidad":23},
             --------------------------------------------------------------------------------
             13:{"nom":"Casado","tipo":"Plato fuerte","precio":3000,"cantidad":23},
             ----------------------------------------------------------------------------------
             14:{"nom":"Arroz con camarones","tipo":"Plato fuerte","precio":5500, "cantidad": 20},
             #entradas en el menu por stock
             15:{"nom":"Dedos de pescado","tipo":"Entrada","precio":3500, "cantidad": 27},
             --------------------------------------------------------------------------------
             16:{"nom":"Porcion de ceviche","tipo":"Entrada","precio": 2000, "cantidad": 24},
             --------------------------------------------------------------------------------
             17:{"nom":"Empanaditas con salsa","tipo":"Entrada","precio":2000, "cantidad": 35},
             ------------------------------------------------------------------------------
             18:{"nom":"Dedos de pescado","tipo":"Entrada","precio":3500, "cantidad": 27},
             --------------------------------------------------------------------------------
             19:{"nom":"Mini patacones","tipo":"Entrada","precio":3250,"cantidad": 39},
             #bebidas en el menu por stock
             20:{"nom":"Coca-Cola Zero","tipo":"Bebida","precio":1500, "cantidad": 45},
             --------------------------------------------------------------------
             21:{"nom":"Coca-Cola","tipo":"Bebida","precio":1500, "cantidad": 67},
             ----------------------------------------------------------------------
             22:{"nom":"Mirinda pina","tipo":"Bebida","precio":1500, "cantidad": 54},
             ----------------------------------------------------------------------
             23:{"nom":"Pina colada","tipo":"Bebida","precio":2350, "cantidad": 37},
             ------------------------------------------------------------------------
             24:{"nom":"Te melocoton","tipo":"Bebida","precio":1500, "cantidad": 58},
             ----------------------------------------------------------------------
             25:{"nom":"Te blanco","tipo":"Bebida","precio":1600, "cantidad": 58},
             --------------------------------------------------------------------
             26:{"nom":"Te verde","tipo":"Bebida","precio":1700, "cantidad": 58},
             ------------------------------------------------------------------
             27:{"nom":"Pepsi","tipo":"Bebida","precio":1400, "cantidad": 70},
             --------------------------------------------------------------------
             28:{"nom":"Pepsi Zero","tipo":"Bebida","precio":1400, "cantidad": 68},
             --------------------------------------------------------------------
             29:{"nom":"Monster","tipo":"Bebida","precio":2300, "cantidad": 83},
             #postres por stock
             30:{"nom":"Flan de vainilla","tipo":"Postre","precio":2200, "cantidad": 36},
             ------------------------------------------------------------------------
             31:{"nom":"Flan de fresa","tipo":"Postre","precio":2200, "cantidad": 9},
             --------------------------------------------------------------------------
             32:{"nom":"Palitos de queso","tipo":"Postre","precio":1800, "cantidad": 47},
             ------------------------------------------------------------------------------
             33:{"nom":"Cheescake de vainilla","tipo":"Postre","precio":2600, "cantidad": 47},
             --------------------------------------------------------------------------------
             34:{"nom":"Cheescake de chocolate","tipo":"Postre","precio":2600, "cantidad": 47},
             ----------------------------------------------------------------------------
             35:{"nom":"Helado de vainilla","tipo":"Postre","precio":900, "cantidad": 47},
             ----------------------------------------------------------------------------
             36:{"nom":"Helado de chocolate","tipo":"Postre","precio":900, "cantidad":257},
             --------------------------------------------------------------------------
             37:{"nom":"Helado de fresa","tipo":"Postre","precio":900, "cantidad": 245},
             ----------------------------------------------------------------------------
             38:{"nom":"Helado de galleta","tipo":"Postre","precio":1000, "cantidad": 227},
             ----------------------------------------------------------------------------
             39:{"nom":"Sundae de la casa","tipo":"Postre","precio":1900, "cantidad": 45},
             ----------------------------------------------------------------------------
             40:{"nom":"Postre aleatorio","tipo":"Postre","precio":1720,"cantidad":1000},}
#diccionario mesas
mesas ={1:{"estado": "libre", "cuan": 2, "vip":"vip"},
        ------------------------------------------------
        2:{"estado": "libre", "cuan":3,"vip":"vip"},
        --------------------------------------------------
        3:{"estado": "libre","cuan": 4, "vip":"vip"},
        ------------------------------------------------
        4:{"estado": "libre","cuan": 6, "vip":"vip"},
        ----------------------------------------------
        5:{"estado": "libre","cuan":1, "vip":"vip"},}
#lista vacia de pedidos
pedido =[]

            
def crud_productos():
    while True:
        print("")
        print("========================================")
        print("|      SISTEMA DE PRODUCTOS            |")
        print("========================================")
        print("| 1. Agregar productos")
        print("| 2. Gestionar productos")  #opciones disponibles
        print("| 3. Salir")
        op = input("Ingrese la opcion a seguir = ")  #preguntamos la opcion a elegir

        if op == "1": #si op 1 entonces
             try:
                 codigo = int(input("Codigo del plato = "))
             except ValueError:
                 print("Error: el codigo debe ser un numero.")
                 continue
             nom = input("Ingrese el nombre del plato = ") #nombre producto
             q_es = input("Que tipo de plato es? Entrada/Fuerte/Bebida/Postre = ") #clasificacion de plato/bebida
             try:
                 precio = int(input("Ingrese el precio del plato (sin comas) = "))
                 cantidad = int(input("Cual es la cantidad disponible = "))
             except ValueError:
                 print("Error: el precio y la cantidad deben ser numeros.")
                 continue
             productos[codigo] = {  #esto dice que en libreria de productos la llave es = al codigo
                "nom": nom,  #estas son las clasificaciones dentro de una libreria que van a corresponder al codigo dado anteriormente
                "tipo": q_es, 
                "precio": precio, 
                "cantidad": cantidad,
                "disponible": cantidad > 0 #si cantidad es mayor a 0
             }
             print("")
             input("PRESIONE ENTER PARA CONTINUAR....")  #una peuqeña pausa 
             print("Producto agregado con exito.")

        elif op == "2": #cuando op es 2
            print ("")
            print("========================")
            print("/ LISTADO DE PRODUCTOS /")
            print("========================")
            for codigo, datos in productos.items(): #si codigo/llave esta en los datos de los productos lee todo lo presente en ese codigo en pares
                if datos["cantidad"] >0: # si cantidad mayor a 0 disponible
                    dispo = "Disponible"
                    
                if datos["cantidad"] <=0: # si menor o igual a 0 agotado
                    dispo = "Agotado"

                print("Codigo:", codigo, "\tNombre:", datos["nom"].ljust(20), "\tTipo:", datos["tipo"].ljust(15), "\tPrecio: ₡", str(datos["precio"]).ljust(8), "\tStock:", str(datos["cantidad"]).ljust(5), "\tEstado:", dispo)
                continue
            #salimos de ese bucle con un continue
            input("PRESIONE ENTER PARA CONTINUAR....")  
            print("")
            cambio = input("Desea realizar algun cambio en los productos? si/no = ")
            
            if cambio == "si":     
              print("")                                                 #sistema para modificar cosas dentro de la opcion 2
              cual = input("Que producto desea modificar? Ingrese el codigo = ")
              if cual.isnumeric():
                  cual = int(cual)
              else:
                  print("Error: el codigo debe ser un numero.")
                  continue
              
              if cual in productos: #si codigo ingresado en cual esta en diccionario de productos entonces
                    print("=========================")
                    print("| Modificacion Productos|")
                    print("=========================")    #interfaz
                    print("")
                    print("| 1. Eliminar producto")
                    print("| 2. Modificar cantidad")
                    print("| 3. Modificar precio")
                    print("| 4. Modificar categoria")
                    print("| 5. Modificar nombre")
                    op2 = input("Que accion desea realizar? = ")
                    if op2 == "1":     #condicional dentro de condicional si op es 1 entonces
                        del productos[cual] #eliminar producto del diccionario
                        print("")
                        print("Eliminado con exito.")
                    elif op2 == "2":                   #si op 2 entonces
                       cantidad2 = input("Cual es la nueva cantidad = ")
                       if cantidad2.isnumeric(): # .isnumeric dice que si se ingresa una letra en vez de un numero el prorama no crashee si no que tire mensaje de error
                           productos[cual]["cantidad"] = int(cantidad2)  #pedir la cantidad nueva guardar en variable y despues reemplazar cantidad antigua por la nueva
                           print("")
                           print("Cantidad actualizada.")
                       else:
                           print("Error: la cantidad debe ser un numero.")
                    elif op2 == "3":                      #si op 3 entonces
                        precio2 = input("Cual es el nuevo precio (sin comas) = ")
                        if precio2.isnumeric():
                            productos[cual]["precio"] = int(precio2)      #pedimos nuevo, guardamos y reemplazamos
                            print("")
                            print("Precio actualizado con exito.")
                        else:
                            print("Error: el precio debe ser un numero.")
                    elif op2 == "4":                             # si op 4 entonces
                        q_es2 = input("Cual es la nueva categoria? = ")
                        productos[cual]["tipo"] = q_es2        #pedimos nueva, guardamos y reemplazamos
                        print("")                        
                        print("Categoria actualizada.")
                    elif op2 == "5":
                        nom2 = input("Cual es el nuevo nombre? = ")
                        productos[cual]["nom"] = nom2              #lo mismo de antes
                        print("")
                        print("Nombre actualizado.")
                    else:
                      print("")
                      print("Opcion no valida.") #si opcion no esta imprimir esto
              else:
                  print("")
                  print("Este codigo no existe o no ha sido registrado.")
        elif op == "3": 
          print("")
          input("PRESIONE ENTER PARA CONTINUAR....")  
          break
        else:
          print("\nEsta accion no esta disponible.")  #si el usuario mete una opcion no valida  

def gestion_mesas():
    while True:
        print("")
        print("===========================")
        print("|    SISTEMA DE MESAS     |") 
        print("===========================")
    
        print("\n| 1. Agregar mesa ")
        print("| 2. Consultar mesas")
        print("| 3. Liberar mesa")        #interfaz
        print("| 4. Ocupar mesa")
        print("| 5. Salir")
        op = input("Que opcion desea seguir? = ") #elegir opcion
        if op == "1":
            codigo = input("Ingrese el codigo de la mesa = ")
            if codigo.isnumeric():    #si opcion 1 entonces preguntar codigo y condicional como blindaje para evitar letras en el input
                codigo = int(codigo)
            else:
                print("Error: el codigo debe ser un numero.")
                continue
            estado = input("Defina el estado actual de la mesa = libre|en proceso|ocupada|pendiente de pago|cancelada = ")
            cuantos = input("De cuantas personas es la mesa? = ")
            if cuantos.isnumeric():           #preguntar esatdo de mesa y cuantos hace referencia a cauntas personas van por mesa
                cuantos = int(cuantos)
            else:
                print("Error: la cantidad de personas debe ser un numero.")
                continue
            vip = input("La mesa es VIP? si/no = ") #queria agregar algo mas aunq la verdad al final utilizarle inclui alargarmucho el codigo
            mesas[codigo] = {
                "estado" : estado,
                "cuan" : cuantos,   #la mesa se guarda en libreria con estado,cuantas,y disq vip xd
                "vip" : vip,
                }
            print("")
            input("PRESIONE ENTER PARA CONTINUAR....")  
            print("Mesa agregada con exito.")
        elif op == "2":
            print ("")
            print("========================")
            print("| LISTADO DE MESAS     |")
            print("========================")
            for codigo, datos in mesas.items():   #listado de las mesas actuales y sis cracteristicas
                print(f"ID = {codigo} | Estado = {datos['estado']} | Para {datos['cuan']} personas | Mesa VIP = {datos['vip']}")
        elif op == "3":    
            mesa = input("\nIngrese el codigo de la mesa que desea liberar = ") #pedir codigo de mesa
            if mesa.isnumeric():
                mesa = int(mesa)   #funcion para liberar una mesa 
                if mesa in mesas:
                    mesas[mesa]["estado"] = "libre"  
                    print(f"Mesa {mesa} liberada con exito.")
                else:
                    print("Esta mesa no esta registrada.")
            else:
                print("Error: ingrese solo numeros.")
        elif op == "4":
            mesa = input("\nIngrese el codigo de la mesa a ocupar = ")#codigo de mesa a cambiar
            if mesa.isnumeric():
                mesa = int(mesa)
                if mesa in mesas:
                    mesas[mesa]["estado"] = "ocupada"#condicional o funcion para cambiarle el estado a ocupada
                    print(f"Mesa {mesa} marcada como ocupada.")
                else:
                    print("Esta mesa no esta registrada.")
            else:                    #msj en caso de tonteras
                print("Error: ingrese solo numeros.")
        elif op == "5":
            print("\n PRESIONA ENTER PARA CONTINUAR")
            break
        else: 
            print("Esta opcion no esta disponible.")

def crud_pedidos():
    while True:
        print("\n===========================")
        print("|      SISTEMA PEDIDOS       |")
        print("=============================")
        print("| 1. Agregar pedidos")
        print("| 2. Consultar pedidos")  #interfaz pedidos
        print("| 3. Modificar pedidos")
        print("| 4. Salir")
        print("")
        op = input("Inserte la opcion que desea seguir = ")
        if op == "1":
            print("")
            print("--- PRODUCTOS DISPONIBLES ---")
            for cod, dat in productos.items():         #si opcion 1 entonces desplegar para agregar productos           
                est = "Disponible" if dat["cantidad"] > 0 else "Agotado"   #si codigo en datos de prodcutos estado disponible si cantidad mayor a 1 si no agotado 
                print("Codigo:", cod, "\tNombre:", dat["nom"].ljust(15), "\tTipo:", dat["tipo"].ljust(10), "\tPrecio: ₡", str(dat["precio"]).ljust(4), "\tStock:", dat["cantidad"], "\tEstado:", est)
            print("")
            mesa = input("Ingrese el numero de mesa = ")
            if mesa.isnumeric():
                mesa = int(mesa)
            else:
                print("Error: ingrese solo numeros.")
                continue
            if mesa in mesas:
                print("")
                codigo = input("Ingrese el codigo del producto = ")
                if codigo.isnumeric():
                    codigo = int(codigo)
                else:
                    print("Error: ingrese solo numeros.")
                    continue
                if codigo in productos:
                    cantidad = input("Ingrese la cantidad requerida = ")
                    if cantidad.isnumeric():
                        cantidad = int(cantidad)
                    else:
                        print("Error: ingrese solo numeros.")
                        continue
                    if cantidad <= 0:
                        print("La cantidad debe ser mayor a cero.")
                    elif productos[codigo]["cantidad"] >= cantidad: #sistema para rebajar de cantidad disponible en pedidos las cantidades solicitadas por el clinte
                        productos[codigo]["cantidad"] -= cantidad

                        if productos[codigo]["cantidad"] == 0:
                            productos[codigo]["disponible"] = False #si productos son 0 entonces decir agotado
                        
                        precio = productos[codigo]["precio"]
                        pedido.append({
                            "mesa": mesa,
                            "codigo":codigo,
                            "producto":productos[codigo]["nom"],#cantidad/codigo/ a cual mesa/ precio de esa orden
                            "precio": productos[codigo]["precio"],  #parte del codigo para elborar el pedido completo
                            "cantidad": cantidad,
                            "subtotal": precio * cantidad,
                             })
                        mesas[mesa]["estado"] = "en progreso"
                        print("")               #pedido realizado cambiar mesa a en progreso
                        print("Pedido realizado con exito.")
                        
                    else:
                        print("")   #si el producto solicitado es menor al stock o no hay tirar este msj que uncluye el nombre y las cantidades restantes
                        print(f"No se pudo realizar el pedido. Stock restante de '{productos[codigo]['nom']}' = {productos[codigo]['cantidad']}")
                else:
                    print("")
                    print("Este producto no esta registrado o no existe.") #si producto no esta en diccionario
            else:
                print("") #si numero de mesa no esta en diccionario
                print("Esta mesa no esta registrada.")
        elif op == "2":
            print("")
            print("--- PRODUCTOS DISPONIBLES ---")
            for cod, dat in productos.items():
                est = "Disponible" if dat["cantidad"] > 0 else "Agotado" #agrego el menu aqui por si la persona se equivoco de codigo entonces poder verificar el pedido realizado
                print("Codigo:", cod, "\tNombre:", dat["nom"].ljust(8), "\tTipo:", dat["tipo"].ljust(5), "\tPrecio: ₡", str(dat["precio"]).ljust(2), "\tStock:", dat["cantidad"], "\tEstado:", est)
            print("")
            print("--- CONSULTAS DE PEDIDOS ---")
            print("| 1. Consulta general de pedidos")
            print("| 2. Consulta de pedido a una mesa")
            print("")
            op2 = input("Seleccione una opcion a seguir = ")
            if op2 == "1":
                for items in pedido: #ciclo para leer todo lo que esta dentro de lista pedidos eh imprimir todo
                    print("\n==============================================================")
                    print(items)
            elif op2 == "2":
                mesa = input("Que mesa desea ver los pedidos en curso? = ")
                if mesa.isnumeric():
                    mesa = int(mesa)  #ver pedido de mesa en especifico
                    pedidos_mesa = [p for p in pedido if p["mesa"] == mesa] #recorre toda la lista pedidos identificando las cosas como p de indicie
                    if pedidos_mesa:
                        print(f"\n=== Pedidos de la Mesa {mesa} ===")
                        total = 0 #variable para la factura nos servira para el reporte
                        for p in pedidos_mesa:
                            print(f"  Producto: {p['producto']} | Cantidad: {p['cantidad']} | Subtotal: {p['subtotal']}") #forma de desglosar el pedido en consola dara el nombre catidad y precio ets
                            total += p["subtotal"]
                        print(f"  TOTAL MESA {mesa}: {total}")
                    else:
                        print(f"No hay pedidos registrados para la mesa {mesa}.")
                else:                                         #si no pedido para mesa msj
                    print("Error: ingrese solo numeros.") #en caso de meter letras
            else:
                print("Opcion no valida.") #si se selecciona una opcion no disponible en la interfaz

        elif op == "3":
            print("\n=========================")
            print("|  MODIFICAR PEDIDOS    |")
            print("=========================")   #interfaz
            print("| 1. Modificar cantidad de un producto en un pedido")
            print("| 2. Eliminar un producto de un pedido")
            print("| 3. Eliminar pedido completo de una mesa")
            print("")
            op3 = input("Seleccione una opcion = ")#perdir opcion

            if op3 == "1":
                mesa = input("Ingrese el numero de mesa = ")
                if mesa.isnumeric(): #blindaje
                    mesa = int(mesa)
                else:
                    print("Error: ingrese solo numeros.")
                    continue
                pedidos_mesa = [p for p in pedido if p["mesa"] == mesa]#lo misma identificar los indices p en lista de pedidos
                if pedidos_mesa:
                    print(f"\nPedidos de la mesa {mesa}:")
                    for indice, p in enumerate(pedidos_mesa): 
                        print(f"  [{indice}] {p['producto']} | Cantidad actual: {p['cantidad']}")
                    idx = input("Ingrese el numero del producto a modificar = ")
                    if idx.isnumeric():
                        idx = int(idx) #idx hace referencia al numero de producto
                    else:
                        print("Error: ingrese solo numeros.")
                        continue
                    if 0 <= idx < len(pedidos_mesa):
                        item_real = [p for p in pedido if p["mesa"] == mesa][idx] #los items presentes osea los si existentes son todo
                        nueva_cant = input("Ingrese la nueva cantidad = ") #variable nueva cantidad
                        if nueva_cant.isnumeric():
                            nueva_cant = int(nueva_cant)
                        else:
                            print("Error: ingrese solo numeros.")
                            continue
                        if nueva_cant <= 0: #si la cantidad menor o iual a 0 entonces decir:
                            print("La cantidad debe ser mayor a cero.")
                        else:
                            diferencia = nueva_cant - item_real["cantidad"]
                            if diferencia > 0:
                                if productos[item_real["codigo"]]["cantidad"] >= diferencia: #los mismo de antes si cantidad en stock mayor a 0 seguir
                                    productos[item_real["codigo"]]["cantidad"] -= diferencia #restar el pedido del stock
                                else:
                                    print("No hay suficiente stock disponible.") #si stock es menor al pedido entonces msj
                                    continue
                            else:
                                productos[item_real["codigo"]]["cantidad"] += abs(diferencia)
                            item_real["cantidad"] = nueva_cant    #reemplazar la catidad de item real osea el pedido real del cliente por la cantidad nueva
                            item_real["subtotal"] = nueva_cant * item_real["precio"] #actualizar el precio osea hacer de nuevo el cantidad por el precio anterios deproducto
                            print("Cantidad actualizada con exito.")
                    else:
                        print("Numero de producto no valido.")
                else:
                    print(f"No hay pedidos para la mesa {mesa}.")

            elif op3 == "2":
                mesa = input("Ingrese el numero de mesa = ")
                if mesa.isnumeric(): #numero de mesa a eliminar el producto
                    mesa = int(mesa)
                else:
                    print("Error: ingrese solo numeros.")
                    continue

                        # agarramos todos los pedidos que sean de esta mesa y los metemos en una lista
                pedidos_mesa = [p for p in pedido if p["mesa"] == mesa]
                if pedidos_mesa:
                    print(f"\nProductos en la mesa {mesa}:")
                    # recorremos la lista y le ponemos indice a cada producto para que el usuario sepa cual elegir
                    for i, p in enumerate(pedidos_mesa):
                        print(f"  [{i}] {p['producto']} | Cantidad: {p['cantidad']}")
                    # le pedimos que escriba el numero del producto que quiere borrar
                    idx = input("Ingrese el numero del producto a eliminar = ")
                    # blindaje pa que no meta letras y crashee el programa
                    if idx.isnumeric():                           #en esta parte metemos todo a una sublista ya que mas adelante lo necesito
                        idx = int(idx)                            #para crear el reporte de pedido ventas totales ets
                    else:                                         #xd
                        print("Error: ingrese solo numeros.")
                        continue
                    if 0 <= idx < len(pedidos_mesa): #si num de productos mayor a 0 pero el leido mayor a producto entonces
                        item_real = [p for p in pedido if p["mesa"] == mesa][idx]  #osea que el numero de producto no sea negativo pero tampoco supere a la cantidad pedida
                        productos[item_real["codigo"]]["cantidad"] += item_real["cantidad"] #esto devuelve esos productos al stock original de la tienda
                        pedido.remove(item_real)
                        print("Producto eliminado del pedido con exito.")
                    else:
                        print("Numero de producto no valido.")
                else:
                    print(f"No hay pedidos para la mesa {mesa}.")

            elif op3 == "3":
                mesa = input("Ingrese el numero de mesa a limpiar = ")
                if mesa.isnumeric():   #numero de mesa a eliminar el pedido
                    mesa = int(mesa)
                else:
                    print("Error: ingrese solo numeros.")
                    continue
                pedidos_mesa = [p for p in pedido if p["mesa"] == mesa] #los pedidos de la mesa para devolverla al stock orinal entonces metemos en lista para saber exactamente
                if pedidos_mesa:
                    for p in pedidos_mesa: #los pedidos que se encuentran en la mesa
                        productos[p["codigo"]]["cantidad"] += p["cantidad"]#esto me devuelve los pedidos de esta mesa al stock original
                    pedido[:] = [p for p in pedido if p["mesa"] != mesa]#esto me asegura que este pedido no se guarda en pedidos totales para la hora del repo                          
                    if mesa in mesas:
                        mesas[mesa]["estado"] = "libre"#esto me cambie el estado de mesa a libre porque el pedido fue cancelado
                    print(f"Pedido completo de la mesa {mesa} eliminado con exito.")
                else:
                    print(f"No hay pedidos para la mesa {mesa}.")
            else:
                print("Opcion no valida.") 

        elif op == "4":
            break
        else:
            print("Opcion no valida.")

def reportes():
    while True:
        print("\n========================================")
        print("|         REPORTES DEL DIA             |")
        print("========================================")
        print("| 1. Total de consumo por mesa")
        print("| 2. Total general de ventas del dia")
        print("| 3. Mesas ocupadas y mesas libres")
        print("| 4. Total de pedidos registrados en el dia")
        print("| 5. Salir")
        print("")
        op = input("Seleccione una opcion = ")

        # ver cuanto se gasto en una mesa especifica
        if op == "1":
            mesa = input("Ingrese el numero de mesa = ")
            if mesa.isnumeric():
                mesa = int(mesa)
                # agarramos solo los pedidos que sean de esa mesa
                pedidos_mesa = [p for p in pedido if p["mesa"] == mesa]
                if pedidos_mesa:
                    print(f"\n=== Consumo Mesa {mesa} ===")
                    total = 0
                    # recorremos cada producto del pedido y sumamos el subtotal
                    for p in pedidos_mesa:
                        print(f"  {p['producto']} x{p['cantidad']} = {p['subtotal']}")
                        total += p["subtotal"]
                    print(f"  TOTAL: {total}")
                else:
                    print(f"No hay pedidos registrados para la mesa {mesa}.")
            else:
                print("Error: ingrese solo numeros.")

        
        elif op == "2":
            total_general = sum(p["subtotal"] for p in pedido)
            print(f"\n=== Total General de Ventas del Dia ===") #suma todo lo vendido en el dia de una vez ya que todos estos pedidos estaban siendo uardados en una lista/variable
            print(f"  TOTAL GENERAL: {total_general}")

        
        elif op == "3":
            print("\n=== Estado de Mesas ===")
            ocupadas = []# ver que mesas estan ocupadas y cuales libre
            libres = []

            for codigo, datos in mesas.items():
                if datos["estado"] in ["libre"]: # recorre todas las mesas y las separa segun su estado
                    libres.append(codigo)
                else:
                    ocupadas.append(codigo)
            print(f"  Mesas OCUPADAS ({len(ocupadas)}): {ocupadas}") #cuando lee que estan ocupadas en el diccionario se quedan asi
            print(f"  Mesas LIBRES   ({len(libres)}): {libres}")#si lee libres pasa lo mismo
#esta parte y interfaz pricipal fueron mi dolor de cabeza muchos errores de indentacion muchos errores en nombre que le ponia a las cosas
#mucho dolor para poder asociar esto con la funcion de pedidos y mesas y despues de mcuhoss pero muchosss una exageracion de videos
#y de paginas con ayudas para python guias explicaciones ets
#se logro muchas horas de desveladas en esto y que todo coincidiera
        
        elif op == "4":
            total_pedidos = len(pedido)
            print(f"\n=== Pedidos Registrados en el Dia ===")   #contar cuantos pedidos se hicieron en total y estan registrados en la lista
            print(f"  Total de pedidos: {total_pedidos}")

        
        elif op == "5":
            break  #salir de aqui
        else:
            print("Opcion no valida.")

def menu_principal():
    while True:
        print("\n=========================================")
        print("| ------WELCOME TO JACKSON VILLE-------  |")
        print("=========================================")
        print("| 1. Gestion de Productos (Menu)") #LISTOOO
        print("| 2. Gestion de Pedidos") #LISTOO                  #el corazon de todo (literalmente me hixo sufrir)
        print("| 3. Gestion de Mesas")#listo                      #interfaz pricipal y la que controla hacia dnd dirigerse segun la opcion
        print("| 4. Reportes del Dia")#medio listo                #la ultima pero no menos importante la que le da forma y guia cada movimiento
        print("| 5. Salir")                                       #dentro del codigo o almenos el primeros pasos
                                                                  #disclaimer: segun yo la interfaz principal iba a rriba y me daba demasiados erroeres sufri con ella;-;
        print("")
        op = input("Que opcion desea seguir? = ") #preguntar opcion
        
        if op == "1": crud_productos() #si opcion 1 entrar a funcio productos
        elif op == "2": crud_pedidos() #si opcion 2 entrar a funcio pedidos
        elif op == "3": gestion_mesas() #si opcion 3 entrar a funcio mesas
        elif op == "4": reportes()      #si opcion 4 entrar a funcio reportes
        elif op == "5":
         print("\n------PRESIONE ENTER PARA CONTINUAR-------")
         print("\nFinalizando programa. Buen dia!")
         break  #si opcion 5 salir del programa
        else:
           print("Opcion no valida.")

menu_principal()
