import pandas as pd
from matplotlib import pyplot as plt
import streamlit as st

df = pd.read_excel('table_salary.xlsx')
dfinfl = pd.read_excel('infl.xlsx')
years = df.columns[1:].astype(int)
salary_strointel = df[df['Вид деятельности'] == 'Строительство'].values[0][1:]
salary_hotels = df[df['Вид деятельности'] == 'Гостиницы и рестораны'].values[0][1:]
salary_doctors= df[df['Вид деятельности'] == 'Здравоохранение и предоставление социальных услуг'].values[0][1:]

df_inf = pd.read_excel('infl.xlsx')
inflation = df_inf[df_inf['инфляция'] == 'коэффициент инфляции'].values[0][1:]

def salary_with_inflation(list):
    salary_with_inflation=[]
    salary_with_inflation.append(list[0])
    for i in range(1,len(list)):
        if inflation[i]==0:
            salary_with_inflation.append(list[i-1])
        else:
            salary_with_inflation.append(list[i]*(1+inflation[i]/100))
    return salary_with_inflation

salary_with_inflation_strointel=salary_with_inflation(salary_strointel)
salary_with_inflation_hotels=salary_with_inflation(salary_hotels)
salary_with_inflation_doctor=salary_with_inflation(salary_doctors)

plt.figure(figsize=(15, 7))

plt.subplot(1, 2, 1)
plt.plot(years, salary_strointel, '-', color='green',label='Зарплата строителя')
plt.plot(years, salary_hotels, '-', color='blue',label="Зарплата работников гостиничного дела")
plt.plot(years, salary_doctors, '-', color='red',label='Зарплата врача')

plt.title('Графики изменения номинальной ЗП')

plt.subplot(1, 2, 2)
plt.plot(years, salary_with_inflation_strointel, '-',color='green',label='Зарплата строителя')
plt.plot(years, salary_with_inflation_hotels, '-',color='blue',label="Зарплата работников гостиничного дела")
plt.plot(years, salary_with_inflation_doctor, '-', color='red', label='Зарплата врача')

plt.title('Графики изменения реальной ЗП')
plt.show()

st.title('Сравнение номинальной и реальной ЗП')

st.image('pic1.jpg', caption='Введение')

st.write('Цель проекта: провести сравнение изменения номинальной и реальной зарплат для 3-х видов деятельности: cтроительства, гостиничного и ресторанного дела, здравоохранения и предоставления социальных услуг в период с 2000 по 2023 год')

@st.cache_data
def convert_df(df_1):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df_1.to_csv().encode('utf-8')


csv1 = convert_df(df)
st.write("Данные о зарплате")
st.write(df)
st.download_button(
    label="Скачать данные",
    data=csv1,
    file_name='source_file.csv',
    mime='text/csv',
)

csv2 = convert_df(dfinfl)
st.write("Данные о инфляции:")
st.write(dfinfl)
st.download_button(
    label="Скачать данные",
    data=csv2,
    file_name='source_file_2.csv',
    mime='text/csv',
)

st.write("Изменение номинальной и реальной зарплат в период с 2000 по 2023 год:")

st.pyplot(plt)

st.write('Выводы: зарплаты во всех видах экономических деятельностей выросли, сильнее всего выросла зарплата строителя, меньше всего гостиницы и рестораны. Рост номинальных зарплат имеет положительную тенденцию')