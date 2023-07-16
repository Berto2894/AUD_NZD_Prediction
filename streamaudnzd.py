import pickle
import streamlit as st
import os

model_path = os.path.join(os.path.dirname(__file__), 'audnzdmodel.sav')
Prediksi_model = pickle.load(open(model_path, 'rb'))

#Judul Web
st.title('Prediksi Harga Mata Uang AUD/NZD')

Open = st.text_input('Input Nilai Open')
High = st.text_input('Input Nilai Hight')
Low =  st.text_input('Input Nilai Low')
Close = st.text_input('Input Nilai Close')

Predik = ''

if st.button('Prediksi') :
    Prediksi = Prediksi_model.predict([[Open, High, Low, Close]])
    if(Prediksi[0] == 1):
        Predik = 'Harga Naik'
    else :
        Predik = 'Harga Turun'
    st.success(Predik)
