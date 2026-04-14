 deteccion-fraude-bancario-ml.
Sistema de detección de anomalías en transacciones financieras utilizando Random Forest y Streamlit

 Sistema de Auditoría y Detección de Fraude en Transacciones Financieras

Este repositorio contiene una solución integral de Aprendizaje Automático (Machine Learning) diseñada para la identificación de anomalías y detección de fraudes en transacciones de tarjetas de crédito. El proyecto aborda el desafío técnico del desbalance extremo de clases mediante técnicas de sobremuestreo sintético y evaluación basada en métricas de sensibilidad.

 Estructura del Proyecto

El repositorio se organiza de la siguiente manera:

* **`Deteccion_Fraude_Bancario_ML.ipynb`**: Notebook de Jupyter que contiene el flujo completo de ciencia de datos: Análisis Exploratorio de Datos (EDA), preprocesamiento, balanceo con SMOTE, entrenamiento de modelos (Random Forest y MLP) y evaluación comparativa.
* **`app.py`**: Aplicación web desarrollada con Streamlit que sirve como interfaz de usuario para el procesamiento de lotes de transacciones en tiempo real.
* **`modelo_fraude.pkl`**: Serialización del modelo Random Forest entrenado, listo para producción.
* **`requirements.txt`**: Listado de dependencias y librerías necesarias para la ejecución del entorno.

 Especificaciones Técnicas

* **Algoritmo Principal:** Random Forest Classifier.
* **Técnica de Balanceo:** SMOTE (Synthetic Minority Over-sampling Technique).
* **Métricas Obtenidas (Recall):** 83% en la detección de la clase minoritaria (Fraude).
* **Framework de Despliegue:** Streamlit para la arquitectura Frontend/Backend.

Instalación y Ejecución

Para desplegar este proyecto en un entorno local, siga estos pasos:

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/nombre-del-repo.git](https://github.com/tu-usuario/nombre-del-repo.git)
    cd nombre-del-repo
    ```

2.  **Instalar dependencias:**
    Asegúrese de tener Python instalado y ejecute:
    ```bash
    pip install -r requirements.txt

    pip install streamlit
    ```

3.  **Ejecutar la aplicación:**
    Inicie el servidor de Streamlit con el siguiente comando:
    ```bash
    streamlit run app.py
    ```

    Requisito de Estructura de Archivos

Para garantizar el correcto funcionamiento del sistema de detección, es estrictamente necesario que tanto el script de la aplicación (app.py) como el modelo entrenado (modelo_fraude.pkl) se encuentren localizados en la misma carpeta raíz.

Justificación Técnica:
La arquitectura del software utiliza rutas relativas para la carga del motor de inferencia. Esto significa que el código busca el archivo del modelo en su entorno inmediato; si estos archivos se separan en directorios distintos, el sistema no podrá inicializar el modelo de inteligencia artificial y generará un error de carga (FileNotFoundError) al intentar ejecutar las predicciones.

Ejemplo de organización correcta:

    Carpeta_Proyecto/

        app.py (Script de ejecución)

        modelo_fraude.pkl (Cerebro del modelo)

Metodología

El desarrollo se fundamenta en la comparación de arquitecturas de ensamble frente a redes neuronales profundas. Se priorizó la reducción de falsos negativos (Falsos Negativos) mediante la optimización del Recall, garantizando un sistema robusto para la mitigación de riesgos financieros.

"El dataset no se adjunta en el repositorio de GitHub debido a restricciones de tamaño de la plataforma, pero se incluye en el archivo comprimido final de la entrega."
