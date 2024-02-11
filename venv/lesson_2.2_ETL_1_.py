# Выгрузка данных с сайта
def extract_data(url):
    return pd.read_csv(url)

# Группировка данных
def transform_data(data, group, agreg):
    return data.groupby(group).agg(agreg).reset_index()

# Загрузка в базу данных
# Для тех кто не работал с pandas+sqlite
# data_frame.to_sql(...) автоматически создаст sqlite базу данных и таблицу
def load_data(data, table_name, conn=CON):
    data["insert_time"] = pd.to_datetime("now")
    data.to_sql(table_name, conn, if_exists='replace', index=False)

# Отправка данных на почту
def send_email(data, cred, host, port, to, From):
    _send_email(data=data, cred=cred, host=host, to=to, From=From, port=port)


from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

HOST = "smtp.yandex.ru" # Емейл првоайдер
TO = "stepikairflowcourse@yandex.ru" # Кому
FROM = "stepikairflowcourse@yandex.ru" # От кого

# Красивый вывод таблицы
def html_pretty(df):
    """ Pretty html dataframe
    """
    return """\
    <html>
      <head></head>
      <body>
        {0}
      </body>
    </html>
    """.format(df.to_html())

# Функция отправки из Stack Overflow
def _send_email(data, cred, host, port, to, From):
    """ Send DF to email
    """

    msg = MIMEMultipart()
    part = MIMEText(html_pretty(data), 'html')
    msg.attach(part)

    server = smtplib.SMTP(host, port)
    server.starttls()
    server.login(cred[0], cred[1])
    server.sendmail(From, to, msg.as_string())
    server.quit()  


if __name__ == '__main__':

    # Выгрузка
    data = extract_data(
        "https://raw.githubusercontent.com/dm-novikov/stepik_airflow_course/main/data/data.csv")

    # Трансформация данных
    data = transform_data(data,
                          group=['A', 'B', 'C'],
                          agreg={"D": sum})

    # Загрузка в таблицу
    load_data(data, "table")

    # Отправка на почту (нужны ваши доступы)
    # send_email(data, cred=("stepikairflowcourse", "123456aA-"), host=HOST, port=587, to=TO, From=FROM)    

HOST = "smtp.yandex.ru"
TO = "vadimkawork@yandex.ru"
FROM = "vadimkawork@yandex.ru"

...

send_email(data, cred=("vadimkaworkyandex.ru", "Zxcvbnm,./321"), host=HOST, port=587, to=TO, From=FROM)