import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

from PIL import Image

st.set_page_config(
    page_title="Qazac Legacy",
    page_icon=":tada:",
    layout="wide",
)

st.write("# Bersama Pulih dan Bangkit dari Inflasi serta Kemiskinan untuk Ekonomi Indonesia Tumbuh Kuat")
st.write('by QAZAC LEGACY')
st.write("--------------------------------------------------------------")
st.write("")

image2 = Image.open('./Visualisasi/10 Ratio Penduduk Miskin Tertinggi di Indonesia Tahun 2022.png')
image3 = Image.open('./Visualisasi/Gaji di Provinsi Paling Luas di Indonesia.png')
image14 = Image.open('./Visualisasi/Persebaran Internet di Indonesi Tahun 2022.png')
image18 = Image.open('./Visualisasi/Ratio Persebaran Internet di Indonesia.png')

st.image(image14)
st.write("")
st.write("")
st.write("")    
st.write("") 

st.image(image2)
st.write("")
st.write("")
st.write("")    
st.write("") 

st.image(image3)
st.write("")
st.write("")
st.write("")    
st.write("") 

st.image(image18)
st.write("")
st.write("")
st.write("")    
st.write("") 

inflasi_2018 = pd.read_csv('./Dataset/Inflasi (Umum) - Tahun 1998-2022/Inflasi (Umum) - Tahun 2018.csv')
inflasi_2019 = pd.read_csv('./Dataset/Inflasi (Umum) - Tahun 1998-2022/Inflasi (Umum) - Tahun 2019.csv')
inflasi_2020 = pd.read_csv('./Dataset/Inflasi (Umum) - Tahun 1998-2022/Inflasi (Umum) - Tahun 2020.csv')
inflasi_2021 = pd.read_csv('./Dataset/Inflasi (Umum) - Tahun 1998-2022/Inflasi (Umum) - Tahun 2021.csv')
inflasi_2022 = pd.read_csv('./Dataset/Inflasi (Umum) - Tahun 1998-2022/Inflasi (Umum) - Tahun 2022.csv')

inflasi_2018 = inflasi_2018.drop('_id', axis=1)
inflasi_2019 = inflasi_2019.drop('_id', axis=1)
inflasi_2020 = inflasi_2020.drop('_id', axis=1)
inflasi_2021 = inflasi_2021.drop('_id', axis=1)
inflasi_2022 = inflasi_2022.drop('_id', axis=1)

inflasi_2020 = inflasi_2020.rename(columns={'90 Kota Inflasi (2018=100)': 'Kota Inflasi'})
inflasi_2021 = inflasi_2021.rename(columns={'90 Kota Inflasi (2018=100)': 'Kota Inflasi'})
inflasi_2022 = inflasi_2022.rename(columns={'90 Kota Inflasi (2018=100)': 'Kota Inflasi'})

inflasi_indonesia_2018 = inflasi_2018.set_index('Kota Inflasi')
inflasi_indonesia_2019 = inflasi_2019.set_index('Kota Inflasi')
inflasi_indonesia_2020 = inflasi_2020.set_index('Kota Inflasi')
inflasi_indonesia_2021 = inflasi_2021.set_index('Kota Inflasi')
inflasi_indonesia_2022 = inflasi_2022.set_index('Kota Inflasi')

inflasi_indonesia_2018 = pd.DataFrame(data=inflasi_indonesia_2018.loc['INDONESIA'])
inflasi_indonesia_2019 = pd.DataFrame(data=inflasi_indonesia_2019.loc['INDONESIA'])
inflasi_indonesia_2020 = pd.DataFrame(data=inflasi_indonesia_2020.loc['INDONESIA'])
inflasi_indonesia_2021 = pd.DataFrame(data=inflasi_indonesia_2021.loc['INDONESIA'])
inflasi_indonesia_2022 = pd.DataFrame(data=inflasi_indonesia_2022.loc['INDONESIA'])

inflasi_indonesia = inflasi_indonesia_2018.append([inflasi_indonesia_2019, inflasi_indonesia_2020, inflasi_indonesia_2021, inflasi_indonesia_2022])
inflasi_indonesia = inflasi_indonesia.reset_index().rename(columns={'index': 'Month', 'INDONESIA': 'Value'})

tahun_2022 = inflasi_indonesia[52:]['Value'].sum()

inflasi_indonesia = inflasi_indonesia.set_index('Month').loc['Tahunan'].reset_index()

list_inflasi = inflasi_indonesia['Value'].tolist()

list_inflasi[4] = tahun_2022

data = {'Tahun': ['2018', '2019', '2020', '2021', '2022'], 'Nilai Inflasi': list_inflasi}
inflasi_umum = pd.DataFrame(data=data).set_index('Tahun')

st.write('Inflasi Tahunan Indonesia')
st.line_chart(inflasi_umum)
    
st.write("")
st.write("")
st.write("")
st.write("")

kota_2022 = inflasi_2022['Kota Inflasi'].copy()
month = inflasi_2022.columns[1:10].tolist()

inflasi_2022_sum = inflasi_2022[month].sum(axis=1)

kota_inflasi_2022 = pd.concat([kota_2022, inflasi_2022_sum], axis=1).rename(columns={0: "Inflasi"})

top_10_inflasi_2022 = kota_inflasi_2022.sort_values(by=['Inflasi'], ascending=False)[0:10]

penduduk_miskin = pd.read_csv('./Dataset/Jumlah Penduduk Miskin (Ribu Jiwa) Menurut Provinsi dan Daerah Tahun 2018-2022.csv')
groupby_penduduk_miskin = penduduk_miskin.groupby(['Provinsi', 'Tahunan'])[['Semester 1 (Maret)', 'Semester 2 (September)']].sum().reset_index()

penduduk_miskin_2022 = groupby_penduduk_miskin.loc[groupby_penduduk_miskin['Tahunan'] == 2022].sort_values(by=['Semester 1 (Maret)'], ascending=False)
top_10_kemiskinan_2022 = penduduk_miskin_2022[1:11]

metric_col_1, metric_col_2 = st.columns(2)

with metric_col_1 : 
    st.write('10 kota dengan inflasi tertinggi 2022')
    st.write(top_10_inflasi_2022.reset_index().drop('index', axis=1))

with metric_col_2 : 
    chart = (
    alt.Chart(top_10_inflasi_2022)
    .mark_bar()
    .encode(
        alt.X("Kota Inflasi:O"),
        alt.Y("Inflasi"),
        alt.Color("Kota Inflasi:O"),
        alt.Tooltip(["Kota Inflasi", "Inflasi"]),
    )
    .interactive()
    )
    st.altair_chart(chart)
    
st.write("")
st.write("")
st.write("")    
st.write("") 
    
metric_col_1, metric_col_2 = st.columns(2)

with metric_col_1 : 
    st.write('10 provinsi dengan penduduk miskin 2022')
    st.write(top_10_kemiskinan_2022.reset_index().drop(['index', 'Semester 2 (September)'], axis=1))
    
with metric_col_2 : 
    chart = (
    alt.Chart(top_10_kemiskinan_2022)
    .mark_bar()
    .encode(
        alt.X("Provinsi:O"),
        alt.Y("Semester 1 (Maret)"),
        alt.Color("Provinsi:O"),
        alt.Tooltip(["Provinsi", "Semester 1 (Maret)"]),
    )
    .interactive()
    )
    st.altair_chart(chart)