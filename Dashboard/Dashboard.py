import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

st.title('Belajar Analisis Data')
 
with st.sidebar:
    st.image("https://t3.ftcdn.net/jpg/04/78/04/90/360_F_478049093_rmagQLupEc7LcNXSNdbRxOYWW9HtfMn4.jpg")
    st.text('Toko Sepeda Milik Bangkit \nNama \t\t: Bagas Mujaddid Adyatma \nID Bangkit \t: m004d4ky1573')

#Data awal
day_df = pd.read_csv(r"C:/Users/bagas/Downloads/Bike-sharing-dataset/day.csv")
hour_df = pd.read_csv(r"C:/Users/bagas/Downloads/Bike-sharing-dataset/hour.csv")
#Cleaning Data
day_df['temp'] = day_df['temp'] * 41
day_df['atemp'] = day_df['atemp'] * 50
day_df['hum'] = day_df['hum'] * 100
day_df['windspeed'] = day_df['windspeed'] * 67

day_df['temp'] = day_df['temp'].apply(lambda x: "{:.2f}".format(x))
day_df['atemp'] = day_df['atemp'].apply(lambda x: "{:.2f}".format(x))
day_df['hum'] = day_df['hum'].apply(lambda x: "{:.2f}".format(x))
day_df['windspeed'] = day_df['windspeed'].apply(lambda x: "{:.2f}".format(x))

hour_df['temp'] = hour_df['temp'] * 41
hour_df['atemp'] = hour_df['atemp'] * 50
hour_df['hum'] = hour_df['hum'] * 100
hour_df['windspeed'] = hour_df['windspeed'] * 67
                           
hour_df['temp'] = hour_df['temp'].apply(lambda x: "{:.2f}".format(x))
hour_df['atemp'] = hour_df['atemp'].apply(lambda x: "{:.2f}".format(x))
hour_df['hum'] = hour_df['hum'].apply(lambda x: "{:.2f}".format(x))
hour_df['windspeed'] = hour_df['windspeed'].apply(lambda x: "{:.2f}".format(x))

cat_to_num = ['temp', 'atemp','hum','windspeed']
for column in cat_to_num:
    day_df[column] = day_df[column].astype('float')
    hour_df[column] = hour_df[column].astype('float')


day_df['mnth'] = day_df['mnth'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
})
day_df['season'] = day_df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})
day_df['weekday'] = day_df['weekday'].map({
    0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'
})
day_df['weathersit'] = day_df['weathersit'].map({
    1: 'Clear/Partly Cloudy',
    2: 'Misty/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Severe Weather'
})
day_df['yr'] = day_df['yr'].map({
    0: '2011',
    1: '2012'
})

hour_df['mnth'] = hour_df['mnth'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
})
hour_df['season'] = hour_df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})
hour_df['weekday'] = hour_df['weekday'].map({
    0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'
})
hour_df['weathersit'] = hour_df['weathersit'].map({
    1: 'Clear/Partly Cloudy',
    2: 'Misty/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Severe Weather'
})
hour_df['yr'] = hour_df['yr'].map({
    0: '2011',
    1: '2012'
})

day_df['dteday'] = pd.to_datetime(day_df.dteday)
day_df['season'] = day_df.season.astype('category')
day_df['yr'] = day_df.yr.astype('category')
day_df['mnth'] = day_df.mnth.astype('category')
day_df['holiday'] = day_df.holiday.astype('category')
day_df['weekday'] = day_df.weekday.astype('category')
day_df['workingday'] = day_df.workingday.astype('category')
day_df['weathersit'] = day_df.weathersit.astype('category')

hour_df['dteday'] = pd.to_datetime(day_df.dteday)
hour_df['season'] = hour_df.season.astype('category')
hour_df['yr'] = hour_df.yr.astype('category')
hour_df['mnth'] = hour_df.mnth.astype('category')
hour_df['holiday'] = hour_df.holiday.astype('category')
hour_df['weekday'] = hour_df.weekday.astype('category')
hour_df['workingday'] =hour_df.workingday.astype('category')
hour_df['weathersit'] =hour_df.weathersit.astype('category')

st.header("Berikut merupakan tampilan data dari Dataset yang tersedia")

tab1_1, tab2_1 = st.tabs(["Dataset Day.CSV", "Dataset Hour.CSV"])   

with tab1_1:
    st.write("Berikut merupakan 5 data teratas Dataset Day.CSV")
    st.table(day_df.head())
with tab2_1:
    st.write("Berikut merupakan 5 data teratas Dataset Hour.CSV")
    st.table(hour_df.head())
 
with st.expander("Histogram"):
    tab1, tab2 = st.tabs(["Dataset Day.CSV", "Dataset Hour.CSV"])
    with tab1:
        st.header("Persebaran variabel Numerik Dataset Day.CSV")
    
        for column in cat_to_num:
            plt.figure(figsize=(8,6))
            sns.histplot(day_df[column], kde=True, color='skyblue')
            plt.title('Histogram Variabel Numerik '+column)
            plt.xlabel('Nilai')
            plt.ylabel('Frekuensi') 
            st.pyplot(plt)
 
    with tab2:
        st.header("Persebaran variabel Numerik Dataset Hour.CSV")
        for column in cat_to_num:
            plt.figure(figsize=(8,6))
            sns.histplot(hour_df[column], kde=True, color='skyblue')
            plt.title('Histogram Variabel Numerik '+column)
            plt.xlabel('Nilai')
            plt.ylabel('Frekuensi')
            st.pyplot(plt)
            
st.header("Pengaruh kondisi cuaca terhadap pengguna sepeda")
st.subheader("Pada dataset Day.CSV")
plt.figure(figsize=(10,6))
sns.barplot(x='weathersit',y="cnt",data=day_df)
plt.title('Jumlah Pengguna Sepeda berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Jumlah Pengguna Sepeda')
st.pyplot(plt)
grouped_data_day = day_df.groupby('weathersit')['cnt'].sum()
plt.figure(figsize=(6,6))
plt.pie(grouped_data_day, labels=grouped_data_day.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral', 'lightgreen', 'gold'])
plt.title('Proporsi Pengguna Sepeda berdasarkan kategori kondisi Cuaca')
st.pyplot(plt)

st.subheader("Pada dataset Hour.CSV")
plt.figure(figsize=(10,6))
sns.barplot(x='weathersit',y="cnt",data=hour_df)
plt.title('Jumlah Pengguna Sepeda berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Jumlah Pengguna Sepeda')
st.pyplot(plt)
grouped_data_hour = hour_df.groupby('weathersit')['cnt'].sum()
plt.figure(figsize=(6,6))
plt.pie(grouped_data_hour, labels=grouped_data_hour.index, autopct='%1.5f%%', startangle=90, colors=['skyblue', 'lightcoral', 'lightgreen', 'gold'])
plt.title('Proporsi Pengguna Sepeda berdasarkan kategori kondisi Cuaca')
st.pyplot(plt)

tab2_1,tab2_2 = st.tabs(["Grafik kontinu", "Grafik sejajar"])

with tab2_1:
    st.header("Tren penggunaan sepeda di tiap bulan dalam kurun waktu 2 tahun")
    jumlahbulanan_daydf = day_df.resample(rule='ME', on='dteday').agg({'cnt': 'sum'})
    jumlahbulanan_daydf.index=jumlahbulanan_daydf.index.strftime('%b-%y')
    plt.figure(figsize=(16,6))
    sns.lineplot(x="dteday", y="cnt", data=jumlahbulanan_daydf, color='blue', marker="o")
    plt.xlabel("Bulan-Tahun")
    plt.ylabel("Total Pengguna Sepeda")
    plt.title("Perhitungan bulanan pengguna sepeda (2011-2012)")
    plt.tight_layout()
    st.pyplot(plt)
    
with tab2_2:
    st.header("Tren penggunaan sepeda di tiap bulan dalam kurun waktu 2 tahun yang disejajarkan")
    day_df['mnth'] = pd.Categorical(day_df['mnth'], categories=
    ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],ordered=True)
    jumlah_monthly_d= day_df.groupby(by=["mnth","yr"]).agg({"cnt": "sum"}).reset_index()
    sns.lineplot(data=jumlah_monthly_d,x="mnth",y="cnt",hue="yr",palette="rocket",marker="X",color='blue')
    plt.title("Jumlah total sepeda yang disewakan berdasarkan Bulan dan tahun")
    plt.xlabel("Bulan")
    plt.ylabel("Frekuensi")
    plt.legend(title="Tahun", loc="upper right")
    st.pyplot(plt)
