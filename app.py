##----- Trabajo Parcial-Python Analitycs-----------
# Importamos la Libreria-----------
import streamlit as st

# Generamos el navegador (Menú lateral)
st.sidebar.title("Menú")
modulo = st.sidebar.selectbox("Ir a", ["Página Principal", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])

# Modulo HOME: Presentación del Proyecto ----
if modulo == "Página Principal":
    st.title("Proyecto Módulo 1 – 'Python Fundamentals'")
    st.write("Estudiante: Diego Alfredo Chunga Bonilla - 72433359")
    st.write("Curso: Python Fundamentals")
    st.write("Año: 2026")
    st.write("Aplicación de Streamlit para Programación Orientada a Objetos.")
    st.write("Tecnologías: Python, Streamlit")

# EJERCICIO 1: Variables y Condicionales ----
elif modulo == "Ejercicio 1":
    #Subtitulo de la sección
    st.subheader("Verificador de Presupuesto")
    #Variable ingresar el presupuesto y gasto
    presupuesto = st.number_input("Presupuesto", min_value=0.0)
    gasto = st.number_input("Gasto", min_value=0.0)
    #Función / Condicional para evaluar el presupuesto y gasto
    if st.button("Evaluar"):
        diferencia = presupuesto - gasto
        if gasto < presupuesto:
            st.success("Está dentro del presupuesto")
        elif gasto == presupuesto:
            st.success("El presupuesto es igual al gasto")
        else:
            st.warning("Presupuesto excedido")
        st.write("Se dispone de un déficit de", diferencia)

# EJERCICIO 2: Listas y Diccionarios ----
elif modulo == "Ejercicio 2":
    #Subtitulo de la sección
    st.subheader("Registro de Actividades")
    #Memoria temporal de lista de actividades
    if "actividades" not in st.session_state:
        st.session_state.actividades = []

    #Generamos las variables necesarias para lista de actividades
    #(Nombre y tipo de actividad, presupuesto y gasto)
    nombre = st.text_input("Nombre de actividad financiera")
    tipo = st.text_input("Tipo de actividad")
    presupuesto = st.number_input("Presupuesto actividad", min_value=0.0)
    gasto_real = st.number_input("Gasto real", min_value=0.0)

    #Condicional para agregar actividad
    if st.button("Agregar"):
        actividad = {
            "nombre": nombre,
            "tipo": tipo,
            "presupuesto": presupuesto,
            "gasto_real": gasto_real}
        st.session_state.actividades.append(actividad)
    #Mostramos la lista que se va generando
    st.write(st.session_state.actividades)
    #Recorremos la lista para generar estados (Ingreso - Gasto)
    for a in st.session_state.actividades:
        if a["gasto_real"] <= a["presupuesto"]:
            st.write(a["nombre"], "→ Dentro del presupuesto")
        else:
            st.write(a["nombre"], "→ Excedido")

#  EJERCICIO 3 ----
elif modulo == "Ejercicio 3":
    #Subtitulo de la sección
    st.subheader("Cálculo de Retorno")
    #Generamos variables (Tasa y Meses)
    tasa = st.number_input("Tasa", min_value=0.0)
    meses = st.number_input("Meses", min_value=0)
    #Definimos función de "Cálculo de Retorno"
    def calcular_retorno(a, tasa, meses):
        return a["presupuesto"] * tasa * meses
    #Mostramos los resultados de retorno
    if st.button("Calcular") and "actividades" in st.session_state:
        retornos = list(map(lambda x: calcular_retorno(x, tasa, meses), st.session_state.actividades))
        st.write("Retornos:", retornos)

#  EJERCICIO 4 ----
elif modulo == "Ejercicio 4":
    #Subtitulo de la sección
    st.subheader("Programación Orientada a Objetos")
    #Generamos la clase:
    class Actividad:
        #Atributos de la clase:
        def __init__(self, nombre, tipo, presupuesto, gasto_real):
            self.nombre = nombre
            self.tipo = tipo
            self.presupuesto = presupuesto
            self.gasto_real = gasto_real
        #Método "Está dentro o no del presupuesto"
        def esta_en_presupuesto(self):
            return self.gasto_real <= self.presupuesto
        #Método "Montrar Información Resumen"
        def mostrar_info(self):
            return f"{self.nombre} - {self.tipo} | Presupuesto: {self.presupuesto} | Gasto: {self.gasto_real}"
    #Convertimos los registros a objetos y mostramos la información
    if "actividades" in st.session_state:
        for a in st.session_state.actividades:
            obj = Actividad(a["nombre"], a["tipo"], a["presupuesto"], a["gasto_real"])
            st.write(obj.mostrar_info())
            if obj.esta_en_presupuesto():
                st.success("Dentro del presupuesto")
            else:
                st.warning("Excedido")