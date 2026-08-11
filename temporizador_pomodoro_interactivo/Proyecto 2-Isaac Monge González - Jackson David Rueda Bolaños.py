'''
Curso: Elementos de Computación
Proyecto: #2
Estudiantes: Isaac Monge González - Jackson David Rueda Bolaños
Fecha de entrega: 25/5/2026
'''




from tkinter import *           #se importa la librería
from tkinter import messagebox  #se importa messagebox para mostrar mensajes de error o aviso
import winsound                 #se importa winsound para reproducir sonidos


contador_secuencia = 0          #contador para numerar las secuencias guardadas
secuencia_construida = False    #indica si ya se construyó una secuencia 
tiempo_segundos = 0             #guarda el tiempo en segundos
fase_actual = 'Trabajo'         #define la fase actual
ronda_actual = 1                #define la ronda actual
corriendo = False               #indica si el temporizador está activo
temporizador_id = None          #guarda el id del temporizador


def cargar_datos(t, d, r):                  #carga los datos de una secuencia guardada
    global corriendo, secuencia_construida  #se usan variables globales para controlar el estado
    
    if corriendo:
        messagebox.showerror('Error', 'Secuencia en ejecucion')  #mensaje de error si el temporizador está corriendo
        return                                                   #sale de la función
    
    
    minutos_trabajo.delete(0, END)     #borra el contenido del campo de trabajo
    minutos_trabajo.insert(0, str(t))  #inserta los minutos de trabajo
    
    minutos_descanso.delete(0, END)    #borra el contenido del campo de descanso
    minutos_descanso.insert(0, str(d)) #inserta los minutos de descanso
    
    rondas.delete(0, END)              #borra el contenido del campo de rondas
    rondas.insert(0, str(r))           #inserta la cantidad de rondas


    #actualiza los minutos a la par de trabajo y descanso
    minutos_trabajo_texto.config(text = f'{t}m')   #actualiza el texto de trabajo
    minutos_descanso_texto.config(text = f'{d}m')  #actualiza el texto de descanso


    rondas_totales.config(text = str(r))           #actualiza el total de rondas


    secuencia_construida = True                  #marca que ya hay una secuencia construida



def validar_minutos_rondas():                        #valida que los datos ingresados sean correctos
    global contador_secuencia, secuencia_construida  #usa variables globales
    
    if minutos_trabajo.get() == '' or minutos_descanso.get() == '' or rondas.get() == '':  #verifica que no haya campos vacíos
        messagebox.showerror('Error' , 'Se deben rellenar todos los espacios en blanco')   #mensaje de error si falta un dato
        return                                                                             #sale de la función
    try:
        
        minutos1 = int(minutos_trabajo.get())   #convierte a entero los minutos de trabajo
        minutos2 = int(minutos_descanso.get())  #convierte a entero los minutos de descanso
        cantidad_rondas = int(rondas.get())     #convierte a entero la cantidad de rondas
        
        print(f'Minutos de trabajo: {minutos1}')   #imprime los minutos de trabajo
        print(f'Minutos de descanso: {minutos2}')  #imprime los minutos de descanso
        print(f'Rondas: {cantidad_rondas}')        #imprime la cantidad de rondas


        contador_secuencia += 1                               #aumenta el contador de secuencias
        
        numero_secuencia = f'Secuencia {contador_secuencia}'  #crea el nombre de la secuencia tal que ("Scuencia #")
        
        nuevo_boton = Button(
                            marco_guardar_secuencia, text = numero_secuencia, bg = 'white', relief = 'solid',
                            command = lambda t = minutos1, d = minutos2, r = cantidad_rondas: cargar_datos(t, d, r)
                            )               #crea un botón para guardar la secuencia
        
        nuevo_boton.pack(fill = 'x', pady = 2)  #agrega el botón al panel


        minutos_trabajo.delete(0, END)   #borra el campo de trabajo
        minutos_descanso.delete(0, END)  #borra el campo de descanso
        rondas.delete(0, END)            #borra el campo de rondas
        
        print(f'Secuencia guardada: {numero_secuencia}')        #mensaje de confirmación


        secuencia_construida = True                             #marca que la secuencia ya fue construida


    
    except ValueError:
        messagebox.showerror('Error' , 'Ingrese solo números.')  #mensaje de error si no se ingresan números





def actualizar_reloj():                                 #actualiza el reloj cada segundo
    global tiempo_segundos, temporizador_id, corriendo     #usa variables globales
    
    if corriendo and tiempo_segundos > 0:               #verifica si está corriendo y aún queda tiempo
        
        tiempo_segundos -= 1                            #resta un segundo
        mins, segs = divmod(tiempo_segundos, 60)        #convierte segundos a minutos y segundos
        contador.config(text=f'{mins:02d}:{segs:02d}')  #actualiza el contador
        temporizador_id = ventana_principal.after(1000, actualizar_reloj)     #agenda la siguiente actualización
    
    elif tiempo_segundos == 0 and corriendo:                               #si el tiempo llegó a cero y sigue corriendo
        cambiar_fase()                                                     #cambia de fase llamando la variable cambiar_fase


def iniciar_timer():                                                      #inicia el temporizador
    global corriendo, tiempo_segundos, fase_actual, secuencia_construida  #usa variables globales
    
    #si ya está corriendo, no hace nada
    if corriendo: 
        return                                                            #sale si ya está activo


    #si el tiempo es mayor a cero, venimos de una pausa. 
    if tiempo_segundos > 0:  #si ya había tiempo cargado, reanuda
        
        corriendo = True     #activa el estado de marcha
        actualizar_reloj()   #reanuda el reloj
        return               #sale de la función


    #si el tiempo está en cero, es un inicio desde el principio
    if minutos_trabajo_texto.cget('text') == '0m': #valida que haya una secuencia cargada revisando el texto en pantalla
        messagebox.showerror('Error', 'Selecciona una secuencia guardada o bien, cree una.')  #mensaje de error si no hay secuencia válida
        return  #sale de la función
        
    try:
        if fase_actual == 'Trabajo':                           #si la fase es trabajo
            # Se extraen los minutos quitando la 'm' del final del Label para evitar que falle si el Entry está vacío
            texto_minutos = minutos_trabajo_texto.cget('text').replace('m', '')
            tiempo_segundos = int(texto_minutos) * 60  #convierte minutos a segundos
            contador.config(fg='green')                        #cambia el color del contador
            sonido('inicio')                                   #reproduce sonido de inicio
        
        else:
            # Se extraen los minutos de descanso directamente del Label
            texto_minutos = minutos_descanso_texto.cget('text').replace('m', '')
            tiempo_segundos = int(texto_minutos) * 60          #convierte minutos de descanso a segundos
            contador.config(fg='red')                          #cambia el color del contador
    
    except ValueError:
        messagebox.showerror('Error', 'Selecciona una secuencia guardada o bien, cree una.')  #mensaje de error por valor inválido
        return                                                                                #sale de la función


    corriendo = True    #activa el temporizador
    actualizar_reloj()  #comienza el conteo


def pausar_timer():  #pausa el temporizador
    global corriendo, temporizador_id, tiempo_segundos  #usa variables globales

    if minutos_trabajo_texto.cget('text') == '0m' or (tiempo_segundos == 0 and not corriendo):
        messagebox.showerror('Error', 'Seleccione una secuencia guardada e inicie la sesión.')
        return  #sale de la función
    
    corriendo = False  #detiene el temporizador
    
    if temporizador_id:  #si existe un temporizador programado
        ventana_principal.after_cancel(temporizador_id)  #cancela la siguiente ejecución
        temporizador_id = None  #Limpia el id para evitar duplicados


def pausa_reanudar():  #alternar entre pausa y reanudar
    global corriendo, tiempo_segundos  #usa variables globales
    
    #si la sesion no ha iniciado, no hay accion
    if minutos_trabajo_texto.cget('text') == '0m' or (tiempo_segundos == 0 and not corriendo):
        messagebox.showerror('Error', 'Seleccione una secuencia guardada e inicie la sesión.')
        return  #sale de la función y no hace nada si la sesión no ha arrancado
    
    if corriendo:  #si está corriendo
        pausar_timer()  #lo pausa
    else:
        iniciar_timer()  #lo reanuda o inicia


#se crean las funciones
def sonido(momento):              #reproduce sonidos según el momento
    if momento == 'inicio':
                                  #un tono agudo y corto
        winsound.Beep(1000, 200)  #sonido de inicio
    elif momento == 'fin_trabajo':
        #dos tonos rápidos 
        winsound.Beep(600, 150)   #primer tono de fin de trabajo
        winsound.Beep(1200, 150)  #segundo tono de fin de trabajo
    elif momento == 'fin_descanso':
        #un tono medio más largo
        winsound.Beep(800, 500)   #sonido de fin de descanso
    elif momento == 'fin':
        #tres tonos (final)
        winsound.Beep(1000, 200)  #primer tono final
        winsound.Beep(700, 200)   #segundo tono final
        winsound.Beep(400, 400)   #tercer tono final




def cambiar_fase():  #cambia entre trabajo y descanso
    global fase_actual, ronda_actual, tiempo_segundos, secuencia_construida, corriendo  #usa variables globales
    
    #si la sesion no se ha iniciado, no hay accion
    if minutos_trabajo_texto.cget('text') == '0m' or (tiempo_segundos == 0 and not corriendo):
        messagebox.showerror('Error', 'Seleccione una secuencia guardada e inicie la sesión.')
        return  #sale de la función
    
    pausar_timer()  #pausa el temporizador
    
    try:
        #lee las rondas desde la pantalla ya que el Entry de arriba se borra al guardar
        limite_rondas = int(rondas_totales.cget('text'))
        
        if fase_actual == 'Trabajo':  #si está en trabajo
            fase_actual = 'Descanso'  #cambia a descanso
            label_flecha.place(x = 12, y = 100)  #mueve la flecha
            sonido('fin_descanso')  #reproduce sonido de fin de descanso
        
        else:
            if ronda_actual < limite_rondas:        #si aún no termina todas las rondas
                ronda_actual += 1                   #aumenta la ronda
                fase_actual = 'Trabajo'             #vuelve a trabajo
                label_flecha.place(x = 12, y = 55)  #mueve la flecha
                sonido('fin_trabajo')               #reproduce sonido de fin de trabajo
            else:
                sonido('fin')                       #reproduce sonido final
                resetear_todo()                     #reinicia todo
                messagebox.showinfo('¡Felicidades!' , '¡Sesión Terminada!')  #mensaje final
                return  #sale de la función
        
        tiempo_segundos = 0  #reinicia el tiempo
        iniciar_timer()      #inicia nuevamente
    
    except:
        resetear_todo()      #si hay error, reinicia todo



def resetear_todo():  #reinicia el sistema completo
    global corriendo, tiempo_segundos, fase_actual, ronda_actual, secuencia_construida  #usa variables globales

    #si la sesion no se ha iniciado, no hay accion
    if minutos_trabajo_texto.cget('text') == '0m' or (tiempo_segundos == 0 and not corriendo):
        messagebox.showerror('Error', 'Seleccione una secuencia guardada e inicie la sesión.')
        return  #sale de la función
   

    #detener el reloj de una vez, Guarda el estado en una variable temporal para saber si mostrar el aviso
    estaba_corriendo = corriendo  #guarda si estaba corriendo
    pausar_timer()  #pausa el temporizador
    secuencia_construida = False  #marca la secuencia como no construida

    #reseteamos los valores
    tiempo_segundos = 0  #reinicia el tiempo
    fase_actual = 'Trabajo'  #vuelve a la fase inicial
    ronda_actual = 1  #reinicia la ronda
    label_flecha.place(x = 12, y = 55)  #pone la flecha en su posición inicial

    Label(ventana_principal, text = 'Tiempo restante: ', font = ('Arial', 12, 'bold'), bg = 'white', fg = 'black').place(x = 500, y = 150)  #etiqueta del tiempo restante
    contador.config(text = '00:00', fg = 'black')  #reinicia el contador

    #limpia los textos de la par sin romper los Entry de arriba
    minutos_trabajo_texto.config(text = '0m')      #reinicia el texto de trabajo
    minutos_descanso_texto.config(text = '0m')     #reinicia el texto de descanso
    
    rondas_totales.config(text = '0')              #reinicia el total de rondas

    #aviso, cuando todo está detenido y en cero
    if estaba_corriendo:                           #si estaba corriendo antes de reiniciar
        messagebox.showinfo('Aviso' , 'La sesión se ha detenido y reseteado correctamente')  #mensaje de confirmación



ventana_principal = Tk()    #se crea la ventana principal

ventana_principal.title('Pomodoro')            #se le asigna título a la ventana
ventana_principal.configure(bg='white')        #se configura el color de fondo
ventana_principal.geometry('850x600')          #ajustamos el tamaño de pantalla y la posibilidad de modificar dicho tamaño por el usuario
ventana_principal.resizable(False,False)       #permite redimensionar la ventana



columna_crear_pomodoro = Frame(ventana_principal, bg = ('white'))  #crea la columna para crear pomodoro
columna_crear_pomodoro.place(x = 10 , y = 50)  #ubica la columna en pantalla
marco_crear_pomodoro = LabelFrame(columna_crear_pomodoro, bg='white', padx=10, pady=10, bd=2, relief='solid')  #crea el marco principal
marco_crear_pomodoro.pack()  #muestra el marco
                      
titulo_crear_pomodoro  = Label(marco_crear_pomodoro, text = 'Crear Pomodoro', font = ('Arial', 12, 'bold'), bg = 'white')  #título de la sección
titulo_crear_pomodoro.pack(pady=(0, 10))  #agrega el título con separación


trabajo = Frame(marco_crear_pomodoro, bg = 'White')  #crea el contenedor de trabajo
trabajo.pack(fill = 'x' , pady = 5)  #muestra el contenedor
Label(trabajo, text = 'Trabajo' , bg = 'white', width = 9, anchor = 'w').pack(side = 'left')  #etiqueta de trabajo


minutos_trabajo = Entry(trabajo, relief = 'solid', width = 9)  #campo para minutos de trabajo
minutos_trabajo.pack(side = 'left', padx = 5)  #muestra el campo



descanso = Frame(marco_crear_pomodoro, bg = 'White')  #crea el contenedor de descanso
descanso.pack(fill = 'x' , pady = 5)  #muestra el contenedor
Label(descanso, text = 'Descanso' , bg = 'white', width = 9, anchor = 'w').pack(side = 'left')  #etiqueta de descanso
minutos_descanso = Entry(descanso, relief = 'solid', width = 9,)  #campo para minutos de descanso
minutos_descanso.pack(side = 'left', padx = 5)  #muestra el campo


rondas_2 = Frame(marco_crear_pomodoro, bg = 'White')  #crea el contenedor de rondas
rondas_2.pack(fill = 'x' , pady = 5)  #muestra el contenedor
Label(rondas_2, text = 'Rondas' , bg = 'white', width = 9, anchor = 'w').pack(side = 'left')  #etiqueta de rondas
rondas = Entry(rondas_2, relief = 'solid', width = 9,)  #campo para rondas
rondas.pack(side = 'left', padx = 5)  #muestra el campo


boton_guardar_secuencia = PhotoImage(file = 'boton_guardar_secuencia.gif').subsample(5, 5)  #carga la imagen del botón guardar
boton_guardar = Button(
                    columna_crear_pomodoro, image = boton_guardar_secuencia, relief = 'solid' , bg='white',
                    bd = 0, highlightthickness = 0, command = validar_minutos_rondas
                    )  #crea el botón para guardar la secuencia


boton_guardar.pack(pady=20, padx=45)  #ubica el botón




#guardar secuencias
columna_guardar_secuencia = Frame(ventana_principal, bg = ('white'))  #crea la columna de secuencias guardadas
columna_guardar_secuencia.place(x = 25 , y = 350)  #ubica la columna
marco_guardar_secuencia = LabelFrame(columna_guardar_secuencia, bg='white', padx=10, pady=10, bd=2, relief='solid', )  #crea el marco de guardado
marco_guardar_secuencia.pack()  #muestra el marco


titulo_guardar_secuencia  = Label(marco_guardar_secuencia, text = 'Secuencias Guardadas', font = ('Arial', 9, 'bold'), bg='white')  #título de secuencias guardadas
titulo_guardar_secuencia.pack(pady=(0, 10))  #agrega separación


imagen_play = PhotoImage(file = 'boton_play.gif').subsample(6, 6)  #carga la imagen play
marco_botones = Frame(ventana_principal , bg = 'white')  #crea el contenedor de botones
marco_botones.place(x=450, y=50)  #ubica el contenedor


boton_play = Button(
    marco_botones, 
    image = imagen_play, 
    bg = 'white', 
    activebackground = 'white', 
    bd = 0,                 # Sin bordes
    highlightthicknes = 0 
)  #crea el botón play



boton_play.pack(side='left', padx=10)  #ubica el botón play


imagen_pausa = PhotoImage(file = 'boton_pausa.gif').subsample(6, 6)  #carga la imagen pausa
marco_botones = Frame(ventana_principal , bg = 'white')  #crea el contenedor de botones
marco_botones.place(x=525, y=50)  #ubica el contenedor


boton_pausa = Button(
    marco_botones, 
    image = imagen_pausa, 
    bg = 'white', 
    activebackground = 'white', 
    bd = 0,                 
    highlightthicknes = 0 
)  #crea el botón pausa



boton_pausa.pack(side='left', padx=10)  #ubica el botón pausa


imagen_stop = PhotoImage(file = 'boton_stop.gif').subsample(6, 6)  #carga la imagen stop
marco_botones = Frame(ventana_principal , bg = 'white')  #crea el contenedor de botones
marco_botones.place(x=600, y=50)  #ubica el contenedor


boton_stop = Button(
    marco_botones, 
    image = imagen_stop, 
    bg = 'white', 
    activebackground = 'white', 
    bd = 0,                 
    highlightthicknes = 0
)  #crea el botón stop



boton_stop.pack(side='left', padx=10)  #ubica el botón stop


imagen_next = PhotoImage(file = 'boton_next.gif').subsample(6, 6)  #carga la imagen next
marco_botones = Frame(ventana_principal , bg = 'white')  #crea el contenedor de botones
marco_botones.place(x=675, y=50)  #ubica el contenedor


boton_next = Button(
    marco_botones, 
    image = imagen_next, 
    bg = 'white', 
    activebackground = 'white', 
    bd = 0,                 
    highlightthicknes = 0, 
    
)  #crea el botón next



boton_next.pack(side='left', padx=10)  #ubica el botón next

Label(ventana_principal, text = 'Tiempo restante: ', font = ('Arial', 12, 'bold'), bg = 'white', fg='black').place(x = 500, y = 150)  #etiqueta del tiempo restante
contador = Label(ventana_principal, text = '00:00' , font = ('Arial', 12, 'bold'), bg = 'white')  #contador del tiempo
contador.place(x = 650, y = 150)  #ubica el contador


# Asignar funciones a botones existentes
boton_play.config(command = iniciar_timer)  #asigna iniciar al botón play
boton_pausa.config(command = pausa_reanudar)  #asigna pausa/reanudar al botón pausa
boton_stop.config(command = resetear_todo)  #asigna reset al botón stop
boton_next.config(command = cambiar_fase)  #asigna cambiar fase al botón next



marco_estado_pom = LabelFrame(ventana_principal, text='', bg='white', bd=2, relief='solid')  #crea el marco de estado pomodoro
marco_estado_pom.place(x=450, y=200, width=355, height=150)  #ubica el marco


trabajo = Label(marco_estado_pom, text='Trabajo:', font=('Arial', 25), bg='white', anchor='w')  #etiqueta trabajo
trabajo.place(x=55 , y=50)  #ubica la etiqueta


descanso = Label(marco_estado_pom, text='Descanso:', font=('Arial', 25), bg='white', anchor='w')  #etiqueta descanso
descanso.place(x=55, y=95)  #ubica la etiqueta


imagen_flecha = PhotoImage(file='flecha.gif').subsample(5,5)  #carga la imagen de la flecha
label_flecha = Label(marco_estado_pom, image=imagen_flecha, bg='white')  #crea la flecha
label_flecha.place(x=12, y=55)  #ubica la flecha


# Contadores de minutos a la par con nombres que NO chocan con tus Entry
minutos_trabajo_texto = Label(marco_estado_pom, text='0m', font=('Arial', 20, 'bold'), bg='white', fg='black')  #texto de trabajo
minutos_trabajo_texto.place(x=225, y=55)  #ubica el texto


minutos_descanso_texto = Label(marco_estado_pom, text='0m', font=('Arial', 20, 'bold'), bg='white', fg='black')  #texto de descanso
minutos_descanso_texto.place(x=225, y=100)  #ubica el texto


rondas_totales_txt = Label(marco_estado_pom, text = 'Rondas:', font=('Arial', 15, 'bold'), bg='white', fg='black')  #texto de rondas
rondas_totales_txt.place(x=10 , y=0)  #ubica el texto


rondas_totales = Label(marco_estado_pom, text = '0', font=('Arial', 15, 'bold'), bg='white', fg='black')  #contador de rondas totales
rondas_totales.place(x=95 , y=0)  #ubica el contador


ronda_curso_txt = Label(marco_estado_pom, text = 'En curso:', font=('Arial', 15, 'bold'), bg='white', fg='black')  #texto de ronda en curso
ronda_curso_txt.place(x=210 , y=0)  #ubica el texto


ronda_curso = Label(marco_estado_pom, text = '0', font=('Arial', 15, 'bold'), bg='white', fg='black')  #contador de ronda en curso
ronda_curso.place(x=308 , y=0)  #ubica el contador



def contar_ronda_curso():  #actualiza la ronda en curso
    global ronda_actual , corriendo  #usa variables globales


    if corriendo:  #si está corriendo
        ronda_curso.config(text=str(ronda_actual))  #muestra la ronda actual
    
    else:  #si no está corriendo
        if tiempo_segundos == 0 and fase_actual == 'Trabajo' and ronda_actual == 1:  #si está al inicio
            ronda_curso.config(text='0')  #muestra cero
        
    ventana_principal.after(100, contar_ronda_curso)  #vuelve a llamar la función


contar_ronda_curso()



    
ventana_principal.mainloop()  #se ejecuta todo lo programado