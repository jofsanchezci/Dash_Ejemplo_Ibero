# Tablero: ingresos y educación

Aplicación estática en HTML, CSS y JavaScript, sin dependencias externas ni CDN. Funciona abriendo `index.html` y en cualquier servidor de archivos estáticos.

## Inicio local

Desde esta carpeta, ejecute:

```sh
python3 -m http.server 8000
```

Abra http://localhost:8000. También puede abrir `index.html` directamente.

## Despliegue

Copie `index.html`, `styles.css`, `app.js` y `datos.js` a la carpeta pública de Apache, Nginx u otro servidor estático. Mantenga los cuatro archivos juntos. No necesita Node.js, Python ni una base de datos en producción. Si desea restringir quién puede acceder a los registros, configure la autenticación en su servidor: la aplicación entrega el conjunto completo al navegador.

## Funcionalidades

- Filtros combinados por sexo, nivel educativo y rango de edad.
- Indicadores de cantidad de registros, ingreso medio y mediano, escolaridad media.
- Histograma con 15 intervalos y comparación de ingreso por educación.
- Dispersión con todos los registros, eje intercambiable y correlación de Pearson.
- Cuartiles, desviación estándar muestral y conteo fuera de límites de Tukey (Q1 − 1,5 IQR; Q3 + 1,5 IQR). Estos casos no se eliminan ni se consideran errores automáticamente.
- Tabla ordenable, búsqueda parcial de ID, paginación de 25 filas.
- Exportación CSV de la selección por filtros. La búsqueda de ID solo afecta a la tabla, no a la exportación ni a los gráficos.
- Diseño adaptable, controles con etiquetas y navegación por teclado.

## Datos y metodología

Fuente: `data(20261006-002921).xlsx`, hoja `Sheet1`: 10.280 registros, seis columnas, cero celdas faltantes y cero filas idénticas. Normalización: `Prrimaria completa` → `Primaria completa` (1.823 registros); se conserva el archivo original. `id` es un identificador, no una variable para el análisis. No se asigna moneda porque no figura en la fuente. No se excluyen edades o ingresos extremos.

Los cuartiles usan interpolación lineal sobre posiciones (n−1)p. La desviación estándar usa divisor n−1. La correlación se calcula sobre la selección completa y se muestra como «—» si es indefinida. No se ejecutan predicciones y las asociaciones no prueban causalidad. Los gráficos no muestrean; las superposiciones en dispersión pueden ocultar registros.

## Actualizar el Excel

Ejecute `convertir_datos.py` con Python, pandas y openpyxl instalados:

```sh
pip install pandas openpyxl
python convertir_datos.py /ruta/nuevo_archivo.xlsx
```

Esto reemplaza `datos.js`. Mantenga los nombres y tipos de las columnas. Las cifras de calidad y el nombre de la fuente en la interfaz corresponden al archivo inicial y deben revisarse al cambiar de fuente. Recargue el navegador después de actualizar. Los datos no se sincronizan automáticamente con el Excel.
