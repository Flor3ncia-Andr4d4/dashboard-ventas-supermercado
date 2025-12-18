# Dashboard de Ventas - Análisis de Supermercado
<img width="1880" height="843" alt="captura_dashboard" src="https://github.com/user-attachments/assets/f0391009-dd22-4c2a-a9bf-06449d798faf" />


## Descripción del Proyecto
Herramienta de Inteligencia de Negocios (Business Intelligence) desarrollada para el análisis exploratorio de datos y visualización de indicadores clave de rendimiento (KPIs) en un entorno comercial minorista.

La aplicación procesa un dataset de ventas de supermercado (1000 registros) y permite a los usuarios interactuar con la información mediante filtros dinámicos, facilitando la toma de decisiones basada en datos.

## Características Principales
- **Cálculo de KPIs en tiempo real:** Visualización instantánea de Ingresos Totales, Calificación Promedio y Volumen de Transacciones según los filtros aplicados.
- **Filtrado Dinámico:** Segmentación de datos por Línea de Producto.
- **Visualización Interactiva:** Gráficos de distribución (Donut Chart) y comparativos (Bar Chart) implementados con Plotly Express.
- **Interfaz Personalizada:** Configuración de entorno visual (Tema Oscuro) mediante `.streamlit/config.toml` para mejorar la legibilidad y estética de los datos.
- **Arquitectura Modular:** Código estructurado en funciones para la carga de datos (Backend) y renderizado de interfaz (Frontend).

## Tecnologías Utilizadas
Este proyecto fue desarrollado íntegramente en Python utilizando las siguientes librerías:

- **Python 3.x:** Lenguaje principal.
- **Streamlit:** Framework para el desarrollo de la aplicación web.
- **Pandas:** Manipulación, limpieza y estructuración de datos (Dataframes).
- **Plotly Express:** Generación de gráficos interactivos avanzados.

## Estructura del Repositorio
El proyecto sigue una estructura de archivos estándar para garantizar la mantenibilidad:

├── .streamlit/
│   └── config.toml      # Configuración del tema visual (UI)
├── app.py               # Código fuente principal de la aplicación
├── requirements.txt     # Lista de dependencias del proyecto
├── supermarket_sales.csv # Dataset fuente (Fuente: Kaggle)
└── README.md            # Documentación del proyecto

## Instalación y Ejecución Local

Para ejecutar este proyecto en su máquina local, siga estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/Flor3ncia-Andr4d4/dashboard-ventas-supermercado.git](https://github.com/Flor3ncia-Andr4d4/dashboard-ventas-supermercado.git)

   ## Autor
**Flor**
Estudiante de Tecnicatura en Ciencia de Datos e IA.
