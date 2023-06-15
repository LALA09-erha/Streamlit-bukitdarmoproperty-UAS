# import libary 
import streamlit as st
# import metode
import time
import pandas as pd
import datetime
import matplotlib.pyplot as plt


# pige title
st.set_page_config(
    page_title="Prediksi Saham Bukit Darmon Property",
    page_icon="https://static.vecteezy.com/system/resources/previews/019/607/543/original/beer-mug-graphic-clipart-design-free-png.png",
)


# hide menu
hide_streamlit_style = """



<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>

"""
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">', unsafe_allow_html=True)
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
st.markdown(' <div style="position: fixed; top: 0; left: 0; z-index: 9999; width: 100%; background: rgb(14, 17, 23); ; text-align: center;"><a href="https://github.com/LALA09-erha/kolaborasipro" target="_blank"><button style="border-radius: 12px;position: relative; top:50%; margin:10px;"><i class="fa fa-github"></i> Source Code</button></a></div>', unsafe_allow_html=True)



# insialisasi web
st.markdown("<p style='text-align: center; color: white; margin:0 ; padding:0;'>MENU</p>", unsafe_allow_html=True)
kolom = st.columns((2.2, 0.48, 2.7))
home = kolom[1].button('🏠')
about = kolom[2].button('About')

# home page
if home==False and about==False or home==True and about==False:
    st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Prediksi Saham Bukit Darmon Property</h1>", unsafe_allow_html=True)
    # setting kolom
    with st.expander("Setting"):
        st.write("""Metode Regresi yang digunakan :""")

        model_1 = st.checkbox('K-Neighbors Regressor  (K=6) ', value=True)
        model_2 = st.checkbox('Bagging Regressor (SVR estimator=2) ')
        model_3 = st.checkbox('Random Forest Regressor (depth=8)')

    # col1, col2 = st.columns(2)
    # with col1:
    #     nama = st.text_input("Masukkan Nama",placeholder='Nama')
    # with col2:
    #     umur = st.number_input("Masukkan Umur",max_value=100)
    date = st.date_input("Masukkan Tanggal:",datetime.date(2021, 1, 1))
    # col3,col4 = st.columns(2)
    # with col3:
    #     bp = st.number_input("Tekanan Darah",min_value=0,max_value=1000)
    # with col4:
    #     chol = st.number_input("Kadar Kolesterol",min_value=0,max_value=1000)
    #    Centering Butoon 
    columns = st.columns((2, 0.6, 2))
    sumbit = columns[1].button("Submit")
    if sumbit == True:
        if(model_1 or model_2 or model_3):
            st.success("Masih dalam tahap pengembangan")
        # if(model_1 or model_2 or model_3):
        #     # mengambil date month dan year
        #     date = pd.to_datetime(date)
        #     date = date.strftime("%Y-%m")
        #     # jika date < 2023-01 maka akan mengambil dari csv yang sudah ada
        #     if date <= '2023-12':
        #         data = pd.read_csv("Data/prediksijanuari2023.csv")                
        #         # get index dari date yang diinput di data
                
        #         index = data[data['Month'] == date].index.values.astype(int)[0]
        #         # jika index + 10 > 339 maka mengambil data dari index sampai 339 - 10
        #         if index + 10 > 339:
        #             datas = data.iloc[339-9:340]
        #         else:
        #             datas = data.iloc[index:index+10]
               
        #         # # pisahkan month ke dalam list
        #         month = datas['Month'].tolist()
                
        #         data_select, label= [] , []

        #         if(model_1):
        #             label.append('K-Neighbors Regressor')
        #             data_select.append(datas['KNN'].tolist())
        #         if(model_2):
        #             label.append('Bagging Regressor (SVR)')
        #             data_select.append(datas['SVR'].tolist())
        #         if(model_3):
        #             label.append('Random Forest Regressor')
        #             data_select.append(datas['RF'].tolist())

        #         data_fix = {}
        #         for i in range(len(label)):
        #             data_fix['Month'] = month
        #             data_fix[label[i]] = data_select[i]
        #             # memasukkan bulan ke dalam data_fix
                
        #         # membuat plt untuk menampilkan hasil prediksi
        #         fig, ax = plt.subplots(figsize=(10, 5))
        #         ax.grid(True)
        #         for i in range(len(label)):
        #             ax.plot(month, data_fix[label[i]], label=label[i])
        #         ax.set_xlabel('Month')
        #         ax.set_ylabel('Beer Production')
        #         ax.set_title('Prediksi Saham Bukit Darmon Property')
        #         ax.legend()
        #         st.pyplot(fig)

        #         # # menampilkan hasil prediksi data_fix pada st.table
        #         datas = pd.DataFrame(data_fix)
        #         st_date = datas.head(1)['Month'].values[0]
        #         en_date = datas.tail(1)['Month'].values[0]
        #         st.markdown(f"<h3 style='text-align: center; color: white; margin:0 ; padding:0;'>Hasil Prediksi Saham Bukit Darmon Property Pada {st_date} - {en_date}</h3>", unsafe_allow_html=True)
        #         datas = datas.style.set_properties(**{'text-align': 'center'})
        #         datas = datas.set_table_styles([ dict(selector='th', props=[('text-align', 'center')] ) ])
        #         st.table(datas)
        #     else:
        #         st.warning("Tanggal yang anda masukkan melebihi batas , Masih dalam tahap pengembangan ❤️")

                
        else:
            st.warning("Pilih Metode Regresi")
       

# about page
if about==True and home==False:
    data = pd.read_csv("Data/monthly-beer-production-in-austr.csv")
    url = 'https://www.kaggle.com/datasets/shenba/time-series-datasets?select=monthly-beer-production-in-austr.csv'
    n8 = 'https://github.com/LALA09-erha/kolaborasipro/blob/master/Training%20Model/trainingModelBeerr.ipynb'
    n9 = 'https://github.com/LALA09-erha/kolaborasipro/blob/master/Training%20Model/trainingModelBeerr2.ipynb'


    st.markdown("<h2 style='text-align: center; color: white; margin:0 ; padding:0;'>Tentang Sistem ini</h2>", unsafe_allow_html=True)
    st.write('Sistem ini dibuat oleh FIKRI AINUN NAJIB (200411100153) dan GHANIY ALBAR RASYIDI KUSUMA (200411100166) mahasiswa dari Teknik Informatika, Universitas Trunojoyo Madura.')
    st.write('Sistem ini adalah sebuah sistem yang bertujuan untuk memprediksi produksi minuman beer yang akan dihasilkan oleh sebuah perusahaan beer pada bulan yang akan diprediksi. Sistem ini menggunakan 3 metode yaitu KNN, Bagging, dan Random Forest dan semua metode adalah metode regresi dimana sebuah metode yang berfungsi untuk memprediksi atau memperkirakan pengaruh dari dua atau lebih variabel fungsional tertentu. Sistem ini juga menggunakan dataset yang didapatkan dari Kaggle.com.')
    st.write(' Sistem ini dibuat menggunakan bahasa pemrograman python dan library streamlit.')
    st.markdown("<h4 style='text-align: center; color: white; margin:0 ; padding:0;'>Tentang Dataset</h4>", unsafe_allow_html=True)
    st.markdown("<p  color: white;'>Dataset yang digunakan pada sistem ini memiliki <b>6 fitur</b> termasuk Output (hasil dari cross validation), Dataset yang digunakan dalam sistem ini menggunakan data yang didapatkan melalui repository dataset yang berada pada website Kaggle.com . Dataset yang berjudul <i>Monthly Beer Production in Austr</i>, dataset bertipe timeseries yang digunakan untuk memprediksi produksi minuman beer yang akan dihasilkan oleh sebuah perusahaan beer pada bulan yang akan diprediksi.</p>", unsafe_allow_html=True)
    st.write(' Sesuai dengan nama datasetnya, data yang akan diprediksi berdasarkan bulan. Dataset ini memiliki 2 kolom yaitu Month dan Production. Kolom Month berisi bulan yang akan diprediksi dan kolom Production berisi jumlah Saham Bukit Darmon Property pada bulan tersebut, sehingga pengumpulan data dilakukan setiap bulan.')
    st.write('Data pertama kali diambil pada bulan Januari 1956 dan terakhir pada bulan Agustus 1995 jadi dataset ini memiliki 476 baris data oleh karena itu data yang digunakan sebagai data training sebanyak 381 baris data dan data Testing sebanyak 95 baris data yang diambil secara urut.')
    # menampilkan dataset yang digunakan pada sistem head dan tail dengan sejaar 1
    st.markdown("<p  color: white;'>Berikut adalah contoh data pertama dan data terakhir dari dataset yang digunakan pada sistem ini.</p>", unsafe_allow_html=True)
    # menampilkan secara sejajar 
    data = data.head(1)  , data.tail(1)
    data = pd.concat(data)
    # menampilkan data di tengah
    data = data.style.set_properties(**{'text-align': 'center'})
    data = data.set_table_styles([ dict(selector='th', props=[('text-align', 'center')] ) ])
    st.table(data)
    
    st.markdown("<p  color: white;'>Untuk lebih jelasnya tentang dataset yang digunakan pada sistem ini dapat dilihat pada link berikut.</p>", unsafe_allow_html=True)
    st.info("Dataset : [link](%s)" % url,icon="ℹ️")
    st.markdown("<h4 style='text-align: center; color: white; margin:0 ; padding:0;'>Tahap preprosessing</h4>", unsafe_allow_html=True)
    st.write('Sistem ini menggunakan preprosessing data yaitu dengan normalisasi data, metode normalisasi yang digunakan adalah MinMaxScaler. Selanjutnya data yang sudah dinormalisasi akan dicross validation dengan metode K-Fold Cross Validation dengan nilai K = 6.')
    st.markdown("<h4 style='text-align: center; color: white; margin:0 ; padding:0;'>Metode yang digunakan</h4>", unsafe_allow_html=True)
    st.markdown("<p  color: white;'>Pada sistem ini menggunakan model KNN ( <i>KNeighborsRegressor ) dengan parameter <b>K = 4</b> mendapatkan MAPE (<i>Mean Absolute Percentage Error</i>) 0.07074.</p>", unsafe_allow_html=True)
    st.write('Selanjutnya memakai RandomForestRegressor dengan parameter max depth = 8 mendapatkan MAPE 0.07279.')
    st.write('Terakhir memakai model SVR dengan Bagging Regressor dengan n_estimator = 2 mendapatkan MAPE 0.07518.')
    st.markdown("<h4 style='text-align: center; color: white; margin:0 ; padding:0;'>Penjelasan Singkat</h4>", unsafe_allow_html=True)
    st.write('Metode diatas ialah metode regresi, alasan menggunakan model diatas dengan kondisi parameter yang berbeda karena memiliki MAPE yang kecil. MAPE yang kecil menunjukkan bahwa hasil prediksi yang diberikan oleh model tersebut mendekati nilai aktual. Sebelumnya sudah dilakukan beberapa kali percobaan dan analisa dengan parameter yang berbeda. Untuk lebih jelasnya dapat dilihat pada link berikut.')
    st.info("[Percobaan model pertama](%s) | [Percobaan model Kedua](%s) " % (n8,n9),icon="ℹ️")        