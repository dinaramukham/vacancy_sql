import psycopg2

def wr_sql(info_vacancy):
    """
    записывает полученнцю  инфу в таблицу
    :param info_vacancy: словарь инфу с вакансиями
    :return:
    """
    connect = psycopg2.connect(
        host='localhost',
        database='vacancies',
        user='postgres',
        password='12345'
    )
    cursor = connect.cursor()

    sql_query = """
           INSERT INTO vacancies (
               name_vacancy, company_name, url_vacancy,
               salary_from, salary_to, currency,
               adres, responsibility, requirement
           ) VALUES (
               %(name)s, %(company_name)s, %(url)s, %(from)s, %(to)s,
               %(currency)s, %(address)s, %(responsibility)s, %(requirement)s
           );
       """

    values = {
        "name": info_vacancy.get("name"),
        "url": info_vacancy.get("url"),
        "company_name": info_vacancy.get("company_name"),
        "from": info_vacancy.get("from"),
        "to": info_vacancy.get("to"),
        "currency": info_vacancy.get("currency"),
        "address": info_vacancy.get("address"),
        "responsibility": info_vacancy.get("responsibility"),
        "requirement": info_vacancy.get("requirement")
    }

    cursor.execute(sql_query, values)


    connect.commit()
    cursor.close()
    connect.close()
