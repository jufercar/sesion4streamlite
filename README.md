# Titanic EDA Streamlit App 🚢

Resumen
- Aplicación Streamlit para análisis exploratorio de datos (EDA) diseñada como script reutilizable.
- El entrypoint está en `streamlit/app.py`. Carga por defecto `titanic_clean.csv` (si no existe, genera un dataset sintético) y permite subir CSVs desde la barra lateral.
- Objetivo: proporcionar una herramienta limpia y rápida para explorar, filtrar, visualizar y descargar subconjuntos de datasets tabulares.

Características principales
- Carga de datos: archivo por defecto o upload desde la interfaz.
- Filtros dinámicos: sexo, clase (pclass/class), puerto de embarque, supervivencia, rango de edad y tarifa.
- Visualizaciones interactivas con Plotly: histogramas, barras, boxplots, scatter y mapa de correlación.
- Métricas clave en tiempo real: total de pasajeros, tasa de supervivencia, edad media, tarifa media.
- Generador de gráficos personalizados con validación de entradas.
- Botón para descargar el subconjunto filtrado como CSV.
- Manejo defensivo de errores y mensajes claros en UI.

Requisitos
- Python 3.8+
- Recomendadas:
  - streamlit
  - pandas
  - numpy
  - plotly
  - seaborn
  - scikit-learn (opcional)
  - matplotlib (opcional)

Instalación rápida
1. Clona el repositorio:
   git clone https://github.com/tu_usuario/sesion4streamlite.git

2. Entra en el directorio de la app:
   cd sesion4streamlite/streamlit

3. (Recomendado) crea y activa un entorno virtual:
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux

4. Instala dependencias:
   pip install -r requirements.txt
   (si no existe, usar: pip install streamlit pandas numpy plotly seaborn)

Ejecución
- Desde el directorio `streamlit/`:
  streamlit run app.py

- Nota: la app intentará cargar `titanic_clean.csv`. Si no se encuentra, se ofrece un dataset sintético y se puede subir un CSV propio desde la barra lateral.

Estructura recomendada del repositorio
- streamlit/
  - app.py                # script principal (entrada)
  - requirements.txt      # dependencias recomendadas
  - titanic_clean.csv     # dataset por defecto (opcional)
  - data/                 # ejemplo de datasets (opcional)
  - assets/               # imágenes / logos (opcional)
- 01_preprocesamiento_knn_titanic.py  # script de limpieza e imputación KNN
- README.md

Buenas prácticas y notas del Project Manager
- Incluye un `requirements.txt` reproducible (versiones fijas) antes de publicar.
- Añade un ejemplo `titanic_clean.csv` en `streamlit/` o `streamlit/data/` para facilitar demos.
- Añadir tests básicos (p. ej. que la carga y filtros funcionen con un CSV de ejemplo).
- Considerar muestreo o paginación si se trabaja con CSVs grandes (la app actualmente renderiza tablas completas).
- Documentar en el README comandos de despliegue (Streamlit Cloud, Dockerfile si procede).
- Revisar y fijar versiones de dependencias para entornos de despliegue.

Contribuciones
- Fork -> feature branch -> PR con descripción clara. Incluir capturas o tests cuando aplique.
- Abrir issues para bugs o mejoras de UX/visualización.

Licencia
- Se sugiere MIT para uso educativo; añadir archivo LICENSE si procede.

Contacto
- Mantén el README actualizado con el propietario del repositorio o enlace a issues para soporte.
