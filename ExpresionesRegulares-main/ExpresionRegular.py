""" import streamlit as st
import pandas as pd

st.set_page_config(page_title='Expresiones regulares con datos de Excel', page_icon=':guardsman:', layout='wide')

st.title('Expresiones regulares con datos de Excel')
st.title('Alfredo de Jesús Borraz Juárez - 201244')

df = pd.read_excel("contactos_2023.xlsx")

nombre = st.text_input("Buscar por nombre")

df['Nombre Contacto'] = df['Nombre Contacto'].str.upper()

filtered_df = df[df['Nombre Contacto'].str.contains(nombre.upper(), regex=True, na=False)]

st.write(filtered_df)

 """

import streamlit as st
import pandas as pd

# Función para cargar o actualizar los datos
@st.cache
def load_data(file):
    return pd.read_excel(file)

# Función para mostrar la tabla y realizar operaciones CRUD
def show_table(df):
    st.write(df)

    # Sección CRUD
    st.sidebar.subheader("Operaciones CRUD")
    operacion = st.sidebar.radio("Selecciona una operación:", ("Crear", "Actualizar", "Eliminar"))

    if operacion == "Crear":
        crear_nuevo(df)
    elif operacion == "Actualizar":
        actualizar_registro(df)
    elif operacion == "Eliminar":
        eliminar_registro(df)

# Función para crear un nuevo registro
def crear_nuevo(df):
    st.sidebar.subheader("Crear Nuevo Registro")
    nuevo_nombre = st.sidebar.text_input("Nombre del contacto")
    nuevo_telefono = st.sidebar.text_input("Teléfono del contacto")
    if st.sidebar.button("Agregar"):
        nuevo_registro = pd.DataFrame({"Nombre Contacto": [nuevo_nombre], "Teléfono": [nuevo_telefono]})
        df = pd.concat([df, nuevo_registro], ignore_index=True)
        st.sidebar.success("Registro agregado exitosamente.")
        st.write(df)


# Función para actualizar un registro existente
def actualizar_registro(df):
    st.sidebar.subheader("Actualizar Registro Existente")
    indice_actualizar = st.sidebar.number_input("Índice del registro a actualizar", min_value=0, max_value=len(df)-1, value=0)
    nuevo_nombre = st.sidebar.text_input("Nuevo nombre del contacto", value=df.loc[indice_actualizar, "Nombre Contacto"])
    if "Teléfono" in df.columns:  # Verifica si la columna "Teléfono" está presente en el DataFrame
        nuevo_telefono = st.sidebar.text_input("Nuevo teléfono del contacto", value=df.loc[indice_actualizar, "Teléfono"])
    else:
        nuevo_telefono = ""  # Si la columna no está presente, establece el valor predeterminado como cadena vacía
    if st.sidebar.button("Actualizar"):
        df.loc[indice_actualizar, "Nombre Contacto"] = nuevo_nombre
        df.loc[indice_actualizar, "Teléfono"] = nuevo_telefono
        st.sidebar.success("Registro actualizado exitosamente.")
        st.write(df)


# Función para eliminar un registro existente
def eliminar_registro(df):
    st.sidebar.subheader("Eliminar Registro Existente")
    indice_eliminar = st.sidebar.number_input("Índice del registro a eliminar", min_value=0, max_value=len(df)-1, value=0)
    if st.sidebar.button("Eliminar"):
        df = df.drop(index=indice_eliminar).reset_index(drop=True)
        st.sidebar.success("Registro eliminado exitosamente.")
        st.write(df)

# Configuración de la página
st.set_page_config(page_title='Expresiones regulares con datos de Excel', page_icon=':guardsman:', layout='wide')

# Título de la página
st.title('Recuperación C2 - EXPRESIONES REGULARES DE UNA BUSQUEDA  WEB LOCAL')
st.title('Alfredo de Jesús Borraz Juárez - 201244')

# Cargar datos
df = load_data("datospersonales.xlsx")

# Filtrar por nombre
nombre = st.text_input("Buscar por nombre")
df['Nombre Contacto'] = df['Nombre Contacto'].str.upper()
filtered_df = df[df['Nombre Contacto'].str.contains(nombre.upper(), regex=True, na=False)]

# Mostrar tabla y operaciones CRUD
show_table(filtered_df)
