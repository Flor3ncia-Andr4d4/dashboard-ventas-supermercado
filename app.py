import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------------------------------------------------------
# 1. CONFIGURACIÓN DE LA PÁGINA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Dashboard de Ventas",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 2. FUNCIONES DE CARGA Y DATOS (BACKEND)
# -----------------------------------------------------------------------------
@st.cache_data
def cargar_datos():
    """
    Carga el CSV de ventas y limpia los formatos de fecha.
    Usa caché para que la app sea rápida.
    """
    try:
        # Carga el archivo desde la carpeta local
        df = pd.read_csv('supermarket_sales - Sheet1.csv')
        return df
    except FileNotFoundError:
        return None

# -----------------------------------------------------------------------------
# 3. INTERFAZ DE USUARIO (FRONTEND)
# -----------------------------------------------------------------------------
def mostrar_sidebar(df):
    """Configura la barra lateral con filtros y derechos de autor."""
    
    st.sidebar.header("Filtros Avanzados")
    
    # Filtro: Línea de Producto
    if df is not None:
        lista_productos = ["Todas"] + list(df['Product line'].unique())
        producto_select = st.sidebar.selectbox("Línea de Producto:", lista_productos)
    else:
        producto_select = "Todas"
        
    st.sidebar.markdown("---")
    
    # SECCIÓN DE DERECHOS DE AUTOR
    st.sidebar.info(
        """
        **Dashboard de Ventas v1.0**
        
        Desarrollado por: Florencia Andrada
        Tecnicatura en Ciencia de Datos e IA.
        
        Copyright 2025. Todos los derechos reservados.
        """
    )
    
    return producto_select

def main():
    """Función principal que controla la ejecución de la app."""
    
    # A. Título y Descripción
    st.title("Tablero de Control de Ventas")
    st.markdown("Análisis interactivo de rendimiento comercial y tendencias de productos.")
    st.markdown("---")

    # B. Carga de Datos
    df = cargar_datos()
    
    if df is None:
        st.error("Error Crítico: No se encuentra el archivo 'supermarket_sales - Sheet1.csv'. Verifique la ruta.")
        st.stop()

    # C. Sidebar y Filtros
    producto_filtro = mostrar_sidebar(df)

    # D. Filtrado de Datos
    if producto_filtro != "Todas":
        df_filtrado = df[df['Product line'] == producto_filtro]
    else:
        df_filtrado = df

    # E. KPIs (Métricas Clave)
    total_ventas = df_filtrado['Total'].sum()
    promedio_calificacion = df_filtrado['Rating'].mean()
    total_transacciones = df_filtrado.shape[0]

    col1, col2, col3 = st.columns(3)
    col1.metric("Ingresos Totales", f"${total_ventas:,.2f}")
    col2.metric("Calificación Promedio", f"{promedio_calificacion:.1f}/10")
    col3.metric("Transacciones Totales", total_transacciones)

    st.markdown("---")

    # F. Visualización
    tab1, tab2 = st.tabs(["Gráficos Analíticos", "Base de Datos Detallada"])

    with tab1:
        c1, c2 = st.columns(2)
        
        with c1:
            st.subheader("Distribución por Método de Pago")
            fig_pie = px.pie(
                df_filtrado, 
                values='Total', 
                names='Payment',
                color_discrete_sequence=px.colors.qualitative.Pastel,
                hole=0.4
            )
            st.plotly_chart(fig_pie, use_container_width=True)

        with c2:
            st.subheader("Ventas por Categoría")
            fig_bar = px.bar(
                df_filtrado, 
                x='Product line', 
                y='Total', 
                color='Product line',
                color_discrete_sequence=px.colors.qualitative.Prism,
                template="plotly_white"
            )
            fig_bar.update_layout(showlegend=False)
            st.plotly_chart(fig_bar, use_container_width=True)

    with tab2:
        st.subheader("Detalle de Transacciones")
        st.dataframe(df_filtrado, use_container_width=True)

# -----------------------------------------------------------------------------
# PUNTO DE ENTRADA
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()