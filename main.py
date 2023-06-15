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
    page_icon="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOYAAADbCAMAAABOUB36AAAA2FBMVEX////u7u7t7e2Zyj0Am8lOTk6Zyjv4+Pj19fXx8fH8/Pz29vYAmMhKSko9PT3//v5xcXFCQkLBwcGenp5uvdlft9cInstSsdQWosyTxyuWyTWSxyry8PWw1W34/PL7/fiz13XMzMzW6bjt9t+724Xg7sno8tbS57G/3I2q0mLx+OafzUrc7MLC35PH4Zyl0Fbm697M46bc5cu42X7u8OrM363G3KOx03W/2pbK3qim0VzV5L6t1GctLS2q2eja5cbH5fAAj8XZ7/SYz+SHx+Df59OAgICwsLAT15I3AAAXHElEQVR4nO1dCZfiOJK2cY7JBLq9vdNdXZKVhuEwhzmSTPIimaqeOmb//z9aKUI+kW2Zy8y+jdevWoDt1GcpQp9CIYVhCDG5NFqidCtKTVFqii9vRanVEEW4UJQaULpL3xJfeJe58CqebVyyKowLlFqi9H8L5p2AZHgzf/T88raYDIdPT8PhZPH28jzyZ54AvH/Lfx5M7/H57XVlUcKFpoQQ16X26vXt+dGLKnFemA0ueLko4eWiJC/nImEKwaqkb4kvlFXhrbTx108BoLNt21IK/0HgpUFv7W/4LQ1H59lRJbTrDS/EbIXv0IQr2/ELMcN3CCUzetlm9A7N7DvkBca80WJLAaAaX1YE1tVi5Ik+XPxs2aQV663sKo1Uu2t1legWh5mPb1MOURchtCr8w7FuXx5NbqYc9bPL1Cev3ieAaWaq4k+CfYjQOUE/hUbi/6miM/PLSDDx8559DTAbJjMGi4CblXTNAZ21fZ0s1/35aDTyff7PvL9eTnpbi3IzlLmBf2ctBgY7KUx9o1Ki+NzkvK8IzTQNodPheDTrGjnizUbjydZ2Mx2AuquXDTNPYgzhwpaQOyFQuhWlpig1Rek287PqwjaUDP+JkLiqtjAq28V8locvLbP5YktS/YC/oiffgEq0K1VHeaGh6Iax4jd0uwr72Lo0WUV3tRzlNqFauv5yJVo1foq7/TBZohINXWO4V+8CmKphVgmT3b1bJLQmvBld8tr3qkEMxev3SPJ9ucG7ydrC8NbOgtov3IpGFSPkqWozpsUZid4fNyl9b0eVqIkFiQv7Fkk05G5+FEaU7nyXaFJijY2jWVCuUclX/MSF7COI3rzt2ktNi1MusyV/XNx150yrOrn1zh03ywkzV5if06gu3F7MT4XRAGbbn/ImRXpkudOf4lsNY6is9xH0wDG6kxAkN633/slARuLfJ97ipFsDCzIdrpTwsm1OA9zewJBtcFoZ9OI3ac0vz4KYF71pm9wPTg8wApr8Ox47lAU1hdwKgVI7KsGX7czPYan1HI4htrsV3fUMLRmKvw2tHKXjlrI6pfXGJ5mNuN0bMZOM9FnwcvlqeFNyrQz7Eu9K/fMBDGXOBxUUt+dBJUL10a23hFmNHowsSclssjjBMFkuraUcR21qjy7Egtgy1BZ3erJxskxmu+iPLtnhLCg19CgocNRp2WYnVYWS8YUwguqPQ2tAphvW2O+0hfU22kJQi9Ml5ZfNlm/J7uPuDqTnh4q3c6Ulsn22V7HieifHzfSrUU9/+qHtcdeGc0bzqpR19Mf7yXGzvN4V6QFXS/lCg4tpZVIGQdiVFqxKvSvCfJVq6Q4vC08K7z1PskFJj52JBTFzKocv93K2JyOOMZY46bRhVmBBKiLRThMJqcqbACcM3ALUhVLg9G2KI2iwaevUGwDizRrT0ztP6gXZXtjCZsXbUmkfgOLqTatByodZ9hCi7F0Sklp6aCJo8MBOy4LYgyWNz+SigHJkggafWhznYTCVbCJGubwonFzhA5sNboWHEhYUwgTPCdqhdAmLWNoE6KzgJvbSlCBHxrI9g01RvWWp1dIaULor1EtOPq4FpqBjYPZX3TsxOSwbUHTowZSGFOuKpI/9lk5PxIJYD30+9ZECtfRlv72/qwZTTYHZhIbU51o6rBSpn2TBGirqnoJZ5tZl725kY68MJsxYeD9z31mpOxoklwXdGb4bjpfXBpLLhKCrxj+WBXmS+7xeX1sKeZW8zzuKBTVu0cjS7TViFIJDHZ0eDlMYWdkrrJrZer54SM/IhBXGncSL8mZ2cdu8Yx8uDpg1zrzKBG2HTT5YXG9ufQCXCdanlAV5uHDJacG19lnDCL1T1DuMBbUN457Ci6rHI6KSlurLIarn/WEsqC2HX7q6lracrRVf8rrhTJjTlwNgNtozmLzabi0+vKTAW56tt+5W/ftMjp6zdjHMbMQhhPg1d+FLql8G65VLbKKe7Dpht9vBWKIKyAjDMBUsCJkx7/J1dlnh8R5guJBtu6O8y9CI4AyqGgvqSv+ZV69m+suAYxShjXa++jgerNCJylalB080nEjXIvBu/YWF7Sgl/3LZ9Z6MijB9MRrZwkrXJf6EujSB0aa9go4lDYlfMfxphRyqLpI3GnKMdlqIajwJxUNru8rTTSULYs/QCQof/A8pjZPgSsqsR0gWo1DNAsrpGGvASZ6ZPgtqm+geDIrMzz9/A/nnf58KXSxDMV3eh1nctdD5aFWgB+wFXk2+ARfy699Afjs9TEe4BfYlKL5rhB3whYkPWjA3OJjsCh97PpgGuiczQsuoNVohuhFlrYW/JTZmcVDTOWE6xmhPO0nx2OYYA5iqIFVShm1ldpZgY3L7XShnbU2xMJ1VzdJQMhjqbbqJBhQzalKU1LgZamYJZT8zTN4HM522NAJpJocHphcEjt7sp5KHnrXTOmJxL40yZ3qSFGRu1kZnRYw9azXmmVtzkrVBdFF+k2zOZ1bOgkwGBKhMM88K0zGWe5bW1QlK7oF2rlh5ELgD44+Gwp+zNcf744nW7B79X+7IKQ8C7wEBmpY+8owwRyp2oHXnVPbEZhk9mGkQIJDzwfRTKNEUac2VnJAKzcpYkCMoMGeU5c88G8xZ0sZSe07FrDrHQbInuBSyLmVBAawxrct9BueC6aW6KhkYM4sWOUjSghOVQL0VTqzRo8/6KyqxxjzzTDC7QZIWADqPf6U78/XQgH7F1b849gAkHjfBt6ulCIfDLKQz0xRKHEW6U7dkehILeL+Q5ifjaUFimLCcQHTGqANhOsbEHucDTZGf2HnaK3KQpGSO3mXxF/JZ0Ai6NtV53qGtyeeShC5z+uDQTcyn3WUUsuvoL1YB4SOis6uCwJEFDeMmL5MDYeJMkpCJarhPkR9SxqrVEkNI7lxIbepoY5/VsmqHwRyFzUXcpz2ilSI/BB3hlb3EyOKsdmqvSiqShH3V77OHwfQTqkfde3ifYb805gmUIq5JfPelVRWnA65p92t+EDh7ozpTMJRDYM5SjlcOdJUwdinyQ4OuwPfXvyo8HcTB6Rh9Y/kwV9p29iCYnpX1fFDXArPLTU2a/MA6gfGt06kGUoiwtTafpuSyoAfo1pojcXWY3ZXC+2q7aHa91G8E9PbbzSEw0TPtPphJFpTcwDEnepMTkOowpyqUtoVmN0F+wmCH5qfOzQEwDYieJh/JzSj4g5xWQ9ga1STJFWE6xitRocTGc6098uN0P98cBhN4LR9S8hb+wHFNNEfiqq255/bIFUl+/uzc3BwEEybXdpDHgjxcPdPcw1cRptKRrkaJXp8/BMqDYHZxSPFyYOLAqqmaFWGOkyyOrmh+B3aHQPF+AMqDYBpT0PiRk4CZ2La6rqKaVWA6abcHXRme2O+vFCJmRy3jO6I8DOYSgKyTu3HjcZPdVxg1q7WmnxoTA6EW3XGwt4IpfsTO9EWiPAwmjBj0HhaN9ujBLbihteNjtGE6afIjR35Rm9UeUHwFhvH7UTCFP4v3W9xLlIW5gXV4S3cXsX5rpskPjPxyguXv0kCpLV/BcTANjMGDtbE9mI9iQqptgfRhpsgPhAeIoDTJyAdPyaUvEk5ajoQ5RfYOZYQZbeBowaIC1d41pA0z7fbA5bsfX8S/GL61IKHmxsvuR8IEnkOeIz9XYiscTk/090vrwkyRHxeiGRzjj399/h7FGXpLjKdIrB8cCXNM5CRlnwWxnv6UWogmzBT5kSO/I8b+TudHO64XN7tIfrAzHwkTfD12jynoAc7C9AMR9WCmyI8rZ7IAk+Ps/P4tih2dB/gK8PORMAfA51YqmHfgESPaxzVowcy6PVAcyeQ40j8yN/w4CcwuuPeoGcOMVo02uKNY+1E6MOcp8rMNu2QEcw/GF/n5SJgGUACyiU9mi6bVsAZqa6wJS9GAmXV7xG6fCOZN6oZvHfn5WJhbGwJsRTET/gTTl/LV20hKYTqZNR/4o9/QW5eF+Rce1fmp8wk/HwsTfO84pczQg7mr7aIFKYW5t+bD5RvA2If5R+d7E2aYJ4IpnLU20vMMzD6pMj8pheko1nyM5ucbNczfudn9LrCdCCbMUTCSKBEELszbGGcvp4LJyU9ynQBH/s+dnNYUsOCrE8HEOSUcXJcwt2ZIgqh+ZHshzHTAiwXkx4k6pRrmzclgOgkalBk32SJu5+NhGpOk+SELsLFRpzw3zFAD4eCSxLcCJtJd/bPyCmA6ijUfx/jRuRxMnFhPzgsz7fmRaz7fY907P8xRLkxYMNNd4i+Cmfb8iF1JQr50LgvTtmw6jGFGLAhg6k9QCloz4/nxYM2nk4BxIZj2MAYYjZsnas3cNZ8Lw4y4ToYeTE7Umiryw2F9uihMpHSTXJhHmyAV+TFiWBe1tIsYZqSbJxo3VQEv9cKMg8CFpX07CczevuenDpghC9qLC7qD0O9jOe0w5ROJ5wGXholrfy+KcfO50gqKGuZS5fmpAyauojzvwzQ/yNHzTbXnpw6YSAI+sjA5k/96tPdgz/PD5Us9MCEaXATNJIPAzVbLcGaVVjcVMP3kzi7p+fkr8g5cFuYWXF4zp2XIww+icbMLvk3tSMc9mJmYH/T8hL6dS8MM7ChcNrtUBEvZukvyezA9K+EtoJz8OCLg5eZzLTBhWd7GaLUsTBEXXWH7fwqmk475AfLjND91OvXAnMkgixhmTBJgsVr/+JEkTMfYZsiP6BSfeS3rgemT2JwmgsCFlsp5tfb5I6nWHGY9Pw54fuqC2ac4q1bkQ2HjI9Y37xONmQx4qQkm8vOxckUM42W098bnwLSA/LRkwEtNMFH/RiqYpoexB0fCTHl+6oIpxxMzCxPUlOruzSiAmfb81AQTYjBt6iRi9uLYA7ar5D9QwgwDXv6U1awHJqrfjjXj2INE+NPi8CgvCTMKePnzpk6YSxkfDR/2oqNhjlKyP74YZhTwUi9MWPZzP3JgPriQ3OSQCEyEGXOLWmF2bVjEfcgJAmdWFR60DzMR8FIrTIyntVhOPpTWk2C8hQeRFMHEs0Cd+mHiqt9TS5EPBYLAkSNpKmcWJnh+HBnwUitMjCTt5waBI7HXnItlYMpj6n4YNcN05LlVfKqVuxUuqBDolYbp3sOf+N6pG2YY4hUU5EPBrQt67D0FcxeSn0/1w4xAtLJB4OGGDRw59WhtCmZPbnW6uQKYGPr0kUqKkj5UeROdiFURJmxb+9a5uQKYePYB3RTkQ4EoTHEuhsbUes+z9y1RzRphImUV0Zf5MJ8xm4HO47Iwm5+uAyZEHopzSfIPBOC9VpsIZWC2PneuAqaPk7BNIy8fiiiwV+1dxxmYcupVO0yxe9OmryydOQ5/i0+Y+cBz3DQYQhpmuBxdN0yMpCUfolxwBuYd0neNZc4UzB+ZatYGUx5pj3nW849FQjdm2WFvezBDWLXDxMOOJvEpdDmnP/0kmkPnVcLEQZP8VJ8EHp9JcsvCI3f+A2E6Rk/MqOmU3WbPJNk7Z28OfszytZQrhCmnWHx63yw9A7MLOlzO368RJhoWS+twSDwYqXS//BXCxD3ywv2hkQ8FLy498O0KYS6QAXla+VCcBZ5aX9KcaZgdKTfI+qPPMUz8HMOUF4SwOoWftYS3jzBAC0crH4r5AGdmljVnCubvf4Yiqxl+lLuGfmR+r/pZS7AxyYPmSeCSIpQY2yMOuXJyyscJnimHscI6Z2CaD0TjFMxzH/VZUeSRKxZ5MDVhNnA1pYQKXRlMQYBAM1vKfCgg6fNpzSak7rGLg4SuDSbm4SHdxIHnZmRuc04Cl0fUFk1UJMxf/v33S0jpy+yHR0dXOQkcz6i17G5+ml8J82+/XEJ+/XsxSAeXhyyrWqIQhq5MOsy3hCHMi8gvJTBl7hf3gzXUGTTUME22K7NCVwVTei13rGIKYDmoFMyvrwmmE2CGmgczL1cRiCofCp56nu/9uiaYyGfw1NOqWeHkG8pbOLoimHgqrRU0hcGsmi7tETN02V312Zy/XsTESvmtAKbTxVmm+3hQVji2wG6bk8bn3/91Sfmfgsa8R2IwYaUwFbrZbJiYFMXV381Qg4hNlNDrgsKMjQkXbZIewAvBLAZXnfsuVEzY/d+OG9I0KySNDfMJX20mQ8eQ2ZggMOTg3Lg9zDKxqgWDhjgyCTPmMToYZhdzxvCp55UkwEuJI47pgf6GZ1YVwMxhQaEW/8QFz2vJPp4Wx1hg9chjWd5q8Emn82+azTiLbpg2+fryHIv6jN0wc+ZevWNvl+ok8HQ2VfFC0JFkaaV2uLDMESVZ7NW7Wm5c6Oj3Mm/16NracyQTjPYMZb2rwXSMMKP8lQ2fPlofHAb0YCpZUKjPmGbXFgfTXFF7DtD6yPTEZXmry7KQC32eYY7cq2pPH3usTWcst95F+VAMRW52fHP2FemnTI5ukUG09lOYU76YHoSXSz24Envr4IZ/TLNeWG+jGkxxMsXVjJ9OOJjjMVZaMEtYUMQmovasnQ+FUy9sy7J6Z/Oh3DbTJYwbikrMp7I9D0uFcEJ5Cq2Pz8rrrc6HAlqsYBPcMA+kvaXbWudl3hb7lW0PojjgwnrHUsiComF2ZiFPoHaNA4tvo+eHWjPdekeiebkn+ZCtk8voPLKWxgcyT1SGqdv491L53ftuHUC9Hgn/frV6JyIw2+lSO4pfjErt2+bClQpq6x+5cyJxRIdF4+MuWLtCvTP5UNRsIhFM3RBnntlyZJkYp1xSLwdpLFy5TicWJBtV6q1ND8LnOsZAGiKLBhel8n4QWlhrYKRgnpAFJZ7bvZcd13Yn2qckHC3i1GLkBGgWKsLUZUGJC9mLxMk19CIcl3NYW3Yh231hmepo1Tveq5EpKb/EUnMQyMme7e5KM1geL4MpkdSErAYMa1Gt3vic4ml1YnoavcNF1KBkeGZS5A3dqCkzx1Zp11vC1B1mpUZw3XgMLQIHujyjinaXRIK0SBAfSN+oVu/DYHJh5lv4ki1K12cC2l1SGnYbd2HG24iPhZnDJvZg3jXYz6k4BwlfNORVOuHwAo/yIpDcCEx/sqzN1693cjduupQlEopS+8MilqwH19ETG6PBkIQtye3sRzunElr1PmRAiRWf91wamgebutPTDS/d+S7SCa4Ub2Y7qk7GGOrVuzo9SGkEe5i40Tu3ibU4SZMOFlZoyYUtnzzsZ6I+OwvKhqU+DAVQ6TSl7mqtfbLSnmBKjfUqenO8u7rDmSp09HCY5Y7AsNNmFH82JKGOCjbmbtcHt+lgPY0xwqg8KzeGGg5MHXd07NbNXBjFjXObSGwr0QTWcK7NGkID7c2HQRojt9+OrM6tRnUK3NGyfaqyoKziN43+KrYZYHndYNLX7r+zPoeYxCi6f7/bzDcqleotYVanB3fpW8SF/pAQGQgpDSRxyWoy9gvBeqPxZMsvjCFi3r+hn3y2jpU4BwvKwAR772yed4Qm2hTGGcIxBPeT9Xg+8mczD2Q280fz8XJ4HxBXILQzt+yeG9CV2+eH2dCE2Y4Uv9lg7OFlJzpfst6Q1hya1hX/uYSL+B+l2etAIcnu/YExM/NsfZiqehu5+qxU90xJpfjM8Pqv9h5SHeGmy37te4bOGle1eh/HgtSKb/K28Nc7ir0xNsBFAIXJovdrn997pDE8CwviktdVuv77a8D7Z3G7isPC+TXB04u/73nNffblWVBuVRyDMbZ57C97KyrUkdJ0DjwKxomueov+44ZfWuXZF4bZKDVYUOo+PH68vy2Gvd10u1oFq+30vjdcvL1/PD50j3h2RZhmFJpoxqGJOCUwo8vN6C9kd61AVWIzbqb/Qku06x1vLQa3NEUJbmkxOIJBhPoe8ewK9T4BCzoBUznns41sV4nHn/gdarKgI4fwcz77/2FWqopqk8upYJ7g2QUwY7Nl5lUFs3/FZC9SfLhFi5Bd5tn/C7+f/2V0XeliAAAAAElFTkSuQmCC",
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
st.markdown(' <div style="position: fixed; top: 0; left: 0; z-index: 9999; width: 100%; background: rgb(14, 17, 23); ; text-align: center;"><a href="https://github.com/LALA09-erha/Streamlit-bukitdarmoproperty-UAS" target="_blank"><button style="border-radius: 12px;position: relative; top:50%; margin:10px;"><i class="fa fa-github"></i> Source Code</button></a></div>', unsafe_allow_html=True)



# insialisasi web
st.markdown("<h1 style='text-align: center; color: white; margin:0 ; h1adding:0;'>MENU</h1>", unsafe_allow_html=True)

tab1, tab2, tab3 ,tab4,tab5 = st.tabs(["About","Data", "Preprosessing Data", "Modelling"  ,"Implementasi Model"])

# About Page
with tab1:
    st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>About Model</h1>", unsafe_allow_html=True)
    st.write("Data saham milik  PT Bukit Darmo Property Tbk (BKDP.JK) ini kami dapatkan dari Website yahoo finance berikut link dari dataset (https://finance.yahoo.com/quote/BKDP.JK/history?p=BKDP.JK), dengan panjang data 316.")
    st.write("Tipe data pada dataset saham PT Bukit Darmo Property Tbk (BKDP.JK) ini merupakan tipe data float. Data yang akan diramalkan adalah data volume saham dari PT Bukit Darmo Property Tbk (BKDP.JK). Volume saham sendiri adalah  jumlah aset atau saham, yang berpindah tangan selama beberapa periode waktu, seringkali selama satu hari. volume saham mampu menunjukkan besar kecil atau jumlah transaksi saham, yang diperdagangkan antara pembukaan dan penutupan harian.")
    st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>About Sistem</h1>", unsafe_allow_html=True)
    st.write("Sistem ini dibuat oleh FIKRI AINUN NAJIB (200411100153) dan GHANIY ALBAR RASYIDI KUSUMA (200411100166) mahasiswa dari Teknik Informatika, Universitas Trunojoyo Madura.")
    st.write('Aplikasi ini dibuat dengan tujuan untuk melakukan peramalan terhadap volume saham dari  PT Bukit Darmo Property Tbk (BKDP.JK) per harinya.')


# Data Page
with tab2:
    # Menampilkan data BPDPJK.csv
    st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Data Saham Bukit Darmon Property</h1>", unsafe_allow_html=True)
    dataset = pd.read_csv("Data/BKDP.JK.csv")
    data = dataset.tail(10)
    st.table(data.style.set_properties(**{'text-align': 'center'}))
    st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Data Terpakai</h1>", unsafe_allow_html=True)
    test = dataset['Volume'].tail(5)
    test = test.to_frame()
    st.table(test.style.set_properties(**{'text-align': 'center'}))

# Preprosessing Data Page
with tab3:
    # membuat radio button untuk memilih data dari preprocessing
    st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Preprosessing Data</h1>", unsafe_allow_html=True)
    n8 = 'https://github.com/LALA09-erha/Streamlit-bukitdarmoproperty-UAS/blob/master/Training%20Model/trainingModelPTMinMax2.ipynb'
    n9 = 'https://github.com/LALA09-erha/Streamlit-bukitdarmoproperty-UAS/blob/master/Training%20Model/trainingModelPTPCA2.ipynb'

    st.info("[Percobaan model pertama](%s) | [Percobaan model Kedua](%s) " % (n8,n9),icon="ℹ️")        
    radio = st.radio("",('MinMax', "Reduce Dimension"))
    # jika radio button volume maka akan menampilkan data volume
    if radio == 'MinMax':
        # Menampilkan dataTrainingMinMax.csv
        st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Data Training MinMax</h1>", unsafe_allow_html=True)
        dataset = pd.read_csv("Data/dataTrainingMinmax.csv")
        data = dataset.head(5)
        st.table(data.style.set_properties(**{'text-align': 'center'}))
    else:
        st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Data Training PCA n_component=1</h1>", unsafe_allow_html=True)
        dataset = pd.read_csv("Data/dataTrainingPCA.csv")
        data = dataset.head(5)
        st.table(data.style.set_properties(**{'text-align': 'center'}))

    st.markdown("<p style='text-align: center; color: white; margin:0 ; padding:0;'>Dari preprosessing diatas memutuskan menggunakan Preprosessing <b>MINMAX</b> karena MAPE yang diperoleh dari preprossing MinMax saja mendapatkan nilai yang terkecil.</p>", unsafe_allow_html=True)
    #  menampilkan link

# Modelling Page
with tab4:
    # memanggil data Mape dari file csv
    st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Model Dengan MAPE Terkecil</h1>", unsafe_allow_html=True)
    dataset = pd.read_csv("Data/dataMAPE.csv")
    radio = st.radio("",( "K-Neighbors Regressor  (K=27)", "Decission Tree (depth=3)",'Random Forest Regressor (depth=2)'))
    # jika radio button volume maka akan menampilkan data volume
    if radio == 'K-Neighbors Regressor  (K=27)':
        #menyeleksi dataset model dengan model ['n-7' knn]
        st.markdown("<p style='text-align: center; color: white; margin:0 ; padding:0;'>Data Training K-Neighbors Regressor  (K=27)</p>", unsafe_allow_html=True)
        data = dataset[dataset['model'] == 'n-4 knn']
        st.success(f"MAPE : {data['mape'].values[0]} dengan K = 27 dan n_steps = 4")

        st.markdown("<p style='text-align: center; color: white; margin:0 ; padding:0;'>Contoh Data dengan n_steps 4 yang sudah di MinMax</p>", unsafe_allow_html=True)
        dataset = pd.read_csv("Data/dataN4.csv")
        dataset = dataset.drop(['Unnamed: 0'], axis=1)
        data = dataset.head(10)
        st.table(data.style.set_properties(**{'text-align': 'center'}))

    elif radio == 'Decission Tree (depth=3)':
        st.markdown("<p style='text-align: center; color: white; margin:0 ; padding:0;'>Data Training Decission Tree (depth=3)</p>", unsafe_allow_html=True)
        data = dataset[dataset['model'] == 'n-2 dt']
        st.success(f"MAPE : {data['mape'].values[0]} dengan depth = 3 dan n_steps = 2")
        
    else:
        st.markdown("<p style='text-align: center; color: white; margin:0 ; padding:0;'>Data Training Random Forest Regressor (depth=3)</p>", unsafe_allow_html=True)
        data = dataset[dataset['model'] == 'n-1 rf']
        st.success(f"MAPE : {data['mape'].values[0]} dengan depth = 2 dan n_steps = 1") 

with tab5:
    st.markdown("<h3 style='text-align: center; color: white; margin:0 ; padding:0;'>Penjelasan Singkat</h3>", unsafe_allow_html=True)
    st.write("Pada Sistem ini memutuskan menggunakan model K-Neighbors Regressor  (K=27) dengan n_steps = 4 karena MAPE yang diperoleh dari model tersebut mendapatkan nilai yang terkecil.")
    st.markdown("<h3 style='text-align: center; color: white; margin:0 ; padding:0;'>Prediksi Saham Bukit Darmon Property</h3>", unsafe_allow_html=True)

    date = st.date_input('Masukkan Tanggal Prediksi', value=datetime.date(2023, 6, 16), min_value=datetime.date(2023, 6, 16), max_value=datetime.date(2026, 6, 16))
    # membuat button prediksi di tengah
    columns = st.columns((2, 0.6, 2))
    sumbit = columns[1].button("Submit")
    
    if sumbit == True:
        if(date < datetime.date(2023, 6, 16) and date > datetime.date(2026, 6, 16)):
            st.error("Tanggal yang anda masukkan tidak valid")
        else:   
            data = pd.read_csv("Data/prediksijanuari2023.csv")
            index = data[data['Date'] == str(date)].index.values[0]
            if( index + 10 >= 1098):
                print("masuk")
                datas = data.iloc[index-9:index+1]
            else:
                datas = data.iloc[index:index+10]
            
            dates = datas['Date']
            data_model = datas['Volume']
            fig, ax = plt.subplots(figsize=(15, 5))
            ax.grid(True)
            ax.plot(dates, data_model, label='Data Prediksi Volume Saham Bukit Darmon Property')
            ax.set_xlabel('Days')
            ax.set_ylabel('Stock Volume')
            ax.set_title('Prediksi Saham Bukit Darmon Property')
            ax.legend()
            st.pyplot(fig)
            # # menampilkan hasil prediksi data_fix pada st.table
            st_date = datas.head(1)['Date'].values[0]
            en_date = datas.tail(1)['Date'].values[0]
            st.markdown(f"<h3 style='text-align: center; color: white; margin:0 ; padding:0;'>Hasil Prediksi Saham Bukit Darmon Property Pada {st_date} sampai {en_date}</h3>", unsafe_allow_html=True)
            datas = datas.style.set_properties(**{'text-align': 'center'})
            datas = datas.set_table_styles([ dict(selector='th', props=[('text-align', 'center')] ) ])
            st.table(datas)