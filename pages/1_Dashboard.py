
import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt
from utils.predict import predict_dropout

st.set_page_config(page_title="Dashboard Mahasiswa", layout="wide")

if not st.session_state.get("login"):
    st.warning("⚠️ Silakan login terlebih dahulu melalui halaman utama.")
    st.stop()

st.title("📊 Dashboard Prediksi Dropout")

nama = st.session_state.get("nama_mahasiswa")
df_aktivitas = pd.read_csv("data/aktivitas.csv")
data_mahasiswa = df_aktivitas[df_aktivitas['nama'] == nama].drop(columns=['nama'])

if data_mahasiswa.empty:
    st.error("Data aktivitas tidak ditemukan untuk mahasiswa ini.")
    st.stop()

pred, probas, shap_values, features = predict_dropout(data_mahasiswa)

st.markdown(f"**Nama Mahasiswa:** {nama}")
st.markdown(f"**Status Prediksi:** {'🟢 Tidak Dropout' if pred == 0 else '🔴 Dropout'}")
st.markdown(f"**Probabilitas Risiko Dropout:** `{probas*100:.2f}%`")

if pred == 0:
    st.success("✅ Mahasiswa ini sangat kecil kemungkinannya untuk dropout.")
else:
    st.error("⚠️ Mahasiswa ini memiliki risiko tinggi untuk dropout.")

st.markdown("### 📉 Penjelasan Prediksi (Visualisasi SHAP)")
fig, ax = plt.subplots(figsize=(8, 6))
shap.plots.waterfall(
    shap.Explanation(
        values=shap_values[0],
        base_values=shap_values.base_values[0],
        data=features.iloc[0],
        feature_names=features.columns.tolist()
    ),
    show=False
)
st.pyplot(fig)
