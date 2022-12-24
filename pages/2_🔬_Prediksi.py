from sre_constants import SUCCESS
import streamlit as st
import pickle 
import numpy as np

st.title("Input Data Prediksi Kanker Payudara")

#Load Save Model
model = pickle.load(open('penyakit_kanker.sav', 'rb'))


col1, col2, col3 = st.columns(3)

with col1:
    rataradius = st.text_input('Rata-rata Radius')
with col2:
    ratatekstur = st.text_input('Rata-rata Tekstur')
with col3:
    ratalingkar = st.text_input('Rata-rata Lingkar')
with col1:
    rataarea = st.text_input('Rata-rata Area')
with col2:
    ratakelancaran = st.text_input('Rata-rata Kelancaran')
with col3:
    ratakekompakan = st.text_input('Rata-rata Kekompakan')
with col1:
    ratacekungan = st.text_input('Rata-rata Cekungan')
with col2:
    ratatitikcekung = st.text_input('Rata-rata Titik Cekung')
with col3:
    ratasimetris = st.text_input('Rata-rata Simetris')
with col1:
    ratadimensi = st.text_input('Rata-rata Dimensi Fraktal')
with col2:
    radiusse = st.text_input('Radius SE')
with col3:
    teksturse = st.text_input('Tekstur SE')
with col1:
    lingkaranse = st.text_input('Lingkaran SE')
with col2:
    arease = st.text_input('Area SE')
with col3:
    kelancaranse = st.text_input('Kelancaran SE')
with col1:
    kekompakanse = st.text_input('Kekompakan SE')
with col2:
    cekunganse = st.text_input('Cekungan SE')
with col3:
    titikcekungse = st.text_input('Titik Cekung SE')
with col1:
    simetrisse = st.text_input('Simetris SE')
with col2:
    dimensise = st.text_input('Dimensi Fraktal SE')
with col3:
    radiusterburuk = st.text_input('Radius Terburuk')
with col1:
    teksturterburuk = st.text_input('Tekstur Terburuk')
with col2:
    lingkaranterburuk = st.text_input('Lingkaran Terburuk')
with col3:
    areaterburuk = st.text_input('Area Terburuk')
with col1:
    kelancaranterburuk = st.text_input('Kelancaran Terburuk')
with col2:
    kekompakanterburuk = st.text_input('Kekompakan Terburuk')
with col3:
    cekunganterburuk = st.text_input('Cekungan Terburuk')
with col1:
    titikcekungterburuk = st.text_input('Titik Cekung Terburuk')
with col2:
    simetristerburuk = st.text_input('Simetris Terburuk')
with col3:
    dimensiterburuk = st.text_input('Dimensi Fraktal Terburuk')

#Kode untuk Prediksi
diagnosa_kanker = ''

#Membuat tombol Prediksi
if st.button('Prediksi Penyakit Kanker'):
    prediksi_kanker = model.predict([[rataradius, ratatekstur, ratalingkar, rataarea, ratakelancaran, ratakekompakan, ratacekungan, ratatitikcekung, ratasimetris, ratadimensi,
                                    radiusse, teksturse, lingkaranse, arease, kelancaranse, kekompakanse, cekunganse, titikcekungse, simetrisse, dimensise,
                                    radiusterburuk, teksturterburuk, lingkaranterburuk, areaterburuk,kelancaranterburuk ,kekompakanterburuk, cekunganterburuk, titikcekungterburuk, simetristerburuk, dimensiterburuk]])
    if (prediksi_kanker[0]==1):
        diagnosa_kanker = 'Mengidap Kanker Ganas'
    else:
        diagnosa_kanker = 'Mengidap kanker Jinak'

st.success(diagnosa_kanker)