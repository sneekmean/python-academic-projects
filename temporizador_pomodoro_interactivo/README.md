# ⏳ Proyecto 2: Temporizador Pomodoro Interactiv (basico)

Aplicación de escritorio con interfaz gráfica (GUI) desarrollada para la gestión del tiempo mediante la **técnica Pomodoro**, permitiendo configurar intervalos personalizados de trabajo, descanso y número de rondas.

---

## 🚀 Características Principales

* **Interfaz Gráfica Intuitiva:** Desarrollada con Tkinter para facilitar el control de tiempos de trabajo y descanso.
* **Secuencias Configurables:** Permite al usuario definir minutos de trabajo, descanso y cantidad de rondas, además de guardar múltiples secuencias accesibles desde botones en pantalla.
* **Alertas Sonoras:** Integración con la librería nativa `winsound` para emitir tonos auditivos al iniciar, cambiar de fase (trabajo/descanso) o finalizar la sesión.
* **Panel de Control:**
  * ▶️ **Iniciar / Reanudar:** Comienza o reanuda el conteo regresivo.
  * ⏸️ **Pausar:** Detiene temporalmente el temporizador.
  * ⏹️ **Detener / Reiniciar:** Restablece los contadores y limpia el estado actual.
  * ⏭️ **Siguiente Fase:** Salta manualmente entre intervalos de trabajo y descanso.
* **Indicadores en Tiempo Real:** Muestra visualmente la fase actual (flecha dinámica), el tiempo restante (`00:00`), las rondas totales y la ronda en curso.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Librerías:**
  * `tkinter`: Creación de la interfaz gráfica de usuario y manejo de eventos.
  * `winsound`: Reproducción de frecuencias y sonidos del sistema para avisos.

---

## 👥 Autores

* **Isaac Monge González**
* **Jackson David Rueda Bolaños**
* *Estudiantes de Ingeniería en Electrónica - TEC*[cite: 1]
