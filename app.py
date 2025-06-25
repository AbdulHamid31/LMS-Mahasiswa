
import streamlit as st
import pandas as pd

st.set_page_config(page_title="LMS Dropout", layout="wide")

df = pd.read_csv("data/mahasiswa.csv")

st.title("🎓 Login Mahasiswa")

nim = st.text_input("Masukkan NIM")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user = df[(df["nim"] == nim) & (df["password"] == password)]
    if not user.empty:
        st.success("Login berhasil!")
        st.session_state["login"] = True
        st.session_state["nama_mahasiswa"] = user.iloc[0]["nama"]
        st.experimental_rerun()
    else:
        st.error("NIM atau Password salah.")

if st.session_state.get("login"):
    st.sidebar.success(f"👋 Halo, {st.session_state['nama_mahasiswa']}")
    st.sidebar.markdown("Pilih menu di sidebar untuk mulai ➡️")
