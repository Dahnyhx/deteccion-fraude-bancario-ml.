import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title="Sistema de Auditoría de Fraude", layout="wide")

@st.cache_resource
def load_model():
    return joblib.load('modelo_fraude.pkl')

model = load_model()

st.title("Sistema de Análisis Masivo de Transacciones")
st.markdown("Plataforma de auditoría para la detección de anomalías en flujos de datos transaccionales.")


st.subheader("Carga de Lotes de Datos")
uploaded_file = st.file_uploader("Seleccione el archivo en formato CSV", type=["csv"])

if uploaded_file is not None:
 
    df_input = pd.read_csv(uploaded_file)
    
    st.write(f"Registros identificados en el archivo: {len(df_input)}")
    st.dataframe(df_input.head(), use_container_width=True)

    if st.button("Ejecutar Algoritmo de Detección"):

        X_batch = df_input.drop(['Time', 'Class'], axis=1, errors='ignore')
        

        predictions = model.predict(X_batch)
        probabilities = model.predict_proba(X_batch)[:, 1]
        
   
        df_input['Estado'] = ["ALERTA DE FRAUDE" if p == 1 else "NORMAL" for p in predictions]
        df_input['Probabilidad_Riesgo'] = probabilities
        
 
        st.divider()
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Total Transacciones Analizadas", len(df_input))
            st.metric("Alertas de Riesgo Detectadas", len(df_input[df_input['Estado'] == "ALERTA DE FRAUDE"]))
            
        with col2:
    
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.countplot(x='Estado', data=df_input, palette=['#5DADE2', '#E74C3C'], ax=ax)
            ax.set_title("Distribución de Clasificación")
            st.pyplot(fig)

        st.subheader("Reporte Detallado de Transacciones de Riesgo")
        fraudes_detectados = df_input[df_input['Estado'] == "ALERTA DE FRAUDE"]
        
        if not fraudes_detectados.empty:
       
            st.dataframe(fraudes_detectados.sort_values(by='Probabilidad_Riesgo', ascending=False), use_container_width=True)
            
  
            csv_output = fraudes_detectados.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Exportar Listado de Alertas (CSV)",
                data=csv_output,
                file_name="reporte_fraude_detectado.csv",
                mime="text/csv"
            )
        else:
            st.info("No se han identificado patrones de fraude en el lote analizado.")