import psycopg2
class DBManager():
    def __init__(self):
        self.connect = psycopg2.connect(
            host='localhost',
            database='vacancies',
            user='postgres',
            password='12345'
        )
        self.cursor = self.connect.cursor()

# get_companies_and_vacancies_count()
#  — получает список всех компаний и количество вакансий у каждой компании.
    def get_companies_and_vacancies_count(self):
        self.cursor.execute('select company_name, count(*) from vacancies group by company_name')
        return self.cursor.fetchall()
    # get_all_vacancies()
#  — получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
    def get_all_vacancies(self):
        self.cursor.execute('select company_name, name_vacancy, salary_from, salary_to, url_vacancy from vacancies')
        return self.cursor.fetchall()
    # get_avg_salary()
#  — получает среднюю зарплату по вакансиям.
    def get_avg_salary(self):
        self.cursor.execute('select avg(salary_from) from vacancies ')
        return self.cursor.fetchall()
    # get_vacancies_with_higher_salary()
#  — получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
    def get_vacancies_with_higher_salary(self):
        self.cursor.execute("""select * from vacancies 
                            where salary_from > 
                            (select avg(salary_from) from vacancies)""")
        return self.cursor.fetchall()
# get_vacancies_with_keyword()
#  — получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.
    def get_vacancies_with_keyword(self, name): # psycopg2.errors.UndefinedColumn
        self.cursor.execute(f"select * from vacancies where name_vacancy like '%{name}%'")
        return self.cursor.fetchall()
