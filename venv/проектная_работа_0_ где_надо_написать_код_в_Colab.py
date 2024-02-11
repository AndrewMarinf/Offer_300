# Импорт необходимых библиотек
import pandas as pd
import sqlite3

# Создадим базу данных с которой будем работать
CONN =  sqlite3.connect('sqlite3.db')

# Напишите функцию которая скачивает lданные с гитхаба
# Функция принимает на вход дату
# Функция должна вернуть список словарей или датафрейм, можно(лучше) использовать можно использоват pandas.read_csv()

# С помощью этой функции вы считаете данные по 2 ссылкам
# ссылка на гитхаб с курсами валют - https://github.com/datanlnja/airflow_course/tree/main/excangerate
# ссылка на гитхаб с данными о продажах - https://github.com/datanlnja/airflow_course/tree/main/data

def extract_data(url, date):
  pass

# Напишите функцию которая принимает на вход список словарей, или пандас датафрейм
# и загружает в табличку в sqlite, можно использоват pandas.to_sql()

def insert_to_db(data, table_name, conn):
  pass

# Напишите функцию которая обюъединит данные по ключу или паре ключей
# На выходе возвращает данные, рекомендую использовать pandas.DataFrame

def merge_data(data1, data2, key):
  pass

# Запустите ваш код в функции main
# Напишите генерацию дат, так чтобы у вас получился список
# 2021-01-02, 2021-01-03 ... etc
# Нужны даты с 2021-01-01 по 2021-01-04

dates_list = list(...)

def main(date, conn):

  # Выгружаем данные по валютам и из источника
  currency = extract_data('https://github.com/datanlnja/airflow_course/tree/main/excangerate', date)
  data = extract_data('https://github.com/datanlnja/airflow_course/tree/main/data', date)

  # Оюъедините данные в 1 таблицу
  mg_data = merge_data()

  # Вставляем данные в БД в таблицу data
  insert_to_db(mg_data, 'data')

# Пройдемся по списку дат и выполним скрипт
for date in dates_list:
  main(date, CONN)

# чтобы првоерить решение можете обратиться к вашей базе данных таким образом

import sqlite3

# Создаем подключение к базе данных
conn = sqlite3.connect('sqlite3.db')

# Создаем курсор для выполнения SQL-запросов
cursor = conn.cursor()

# Выполняем запрос к таблице
cursor.execute("SELECT * FROM data")

# Извлекаем все строки из результата запроса
rows = cursor.fetchall()

# Выводим результаты
for row in rows:
    print(row)

# Закрываем соединение
conn.close()






