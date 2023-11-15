import psycopg2
def wr_emp_sql(info_vacancy):
    connect = psycopg2.connect(
        host='localhost',
        database='vacancies',
        user='postgres',
        password='12345'
    )
    with connect.cursor() as  cursor:
        sql_query="""
               INSERT INTO employers (
                   company_name,
                   company_url
                   ) values (
                   %(company_name)s, %(company_url)s);
           """
        values={
            'company_name':info_vacancy.get('company_name'),
            'company_url': info_vacancy.get('company_url')
        }
        cursor.execute(sql_query, values  )
    connect.commit()
    # cursor.close()
    connect.close()
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

    #cursor = connect.cursor()
    with connect.cursor() as  cursor:
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
    #cursor.close()
    connect.close()
def create_sql():

    connect = psycopg2.connect(host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = '12345')

    connect.autocommit = True
    cursor = connect.cursor()
    try:
        cursor.execute(f'DROP DATABASE vacancies WITH (FORCE)') #
    except psycopg2.errors.InvalidCatalogName:
        cursor.execute(f"CREATE DATABASE vacancies")
    else:
        cursor.execute(f"CREATE DATABASE vacancies")
    connect.close()

    connect =psycopg2.connect(host = 'localhost',
    database = 'vacancies',  #
    user = 'postgres',
    password = '12345')
    with connect.cursor() as cur:
        cur.execute("""create table employers(
        company_name text UNIQUE,
        company_url text);
        """)
    with connect.cursor() as cur:
        cur.execute("""create table  vacancies (
        id_vacancy serial, 
        name_vacancy text, 
        company_name text  references employers(company_name), 
        url_vacancy text, 
        salary_from int, 
        salary_to int, 
        currency text, 
        adres text, 
        responsibility text, 
        requirement text);""")
    connect.commit()
    connect.close()

#create_sql()
