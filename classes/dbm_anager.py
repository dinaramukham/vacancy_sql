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
    def print_companies_and_vacancies_count(self):
        #list_info=self.get_companies_and_vacancies_count()
        for index, info in enumerate(self.get_companies_and_vacancies_count()):
            print(f'{index+1}компания: {info[0]} количество вакансий: {info[1]}')
    # get_all_vacancies()
#  — получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
    def get_all_vacancies(self):
        self.cursor.execute('select company_name, name_vacancy, salary_from, salary_to, url_vacancy from vacancies')
        return self.cursor.fetchall()
    def print_all_vacancies(self):
        for index, info in enumerate(self.get_all_vacancies()):
            print(f'{index+1}компания: {info[0]} вакансия: {info[1]} зарплата от: {info[2]} зарплата до: {info[3]} ссылка: {info[4]}')
    # get_avg_salary()
#  — получает среднюю зарплату по вакансиям.
    def get_avg_salary(self):
        self.cursor.execute('select avg(salary_from) from vacancies ')
        return self.cursor.fetchall()
    # get_vacancies_with_higher_salary()
#  — получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
    def get_vacancies_with_higher_salary(self):
        self.cursor.execute("""select name_vacancy, url_vacancy from vacancies 
                            where salary_from > 
                            (select avg(salary_from) from vacancies)""")
        return self.cursor.fetchall()
    def print_vacancies_with_higher_salary(self):
        for index, info in enumerate(self.get_vacancies_with_higher_salary() ):
            print(f'{index+1} вакансия: {info[0]} ссылка: {info[1]} ')
# get_vacancies_with_keyword()
#  — получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.
    def get_vacancies_with_keyword(self, name): # psycopg2.errors.UndefinedColumn
        self.cursor.execute(f"select name_vacancy, url_vacancy from vacancies where name_vacancy like '%{name}%'")
        return self.cursor.fetchall()
    def print_vacancies_with_keywor(self, name):
        for index, info in enumerate(self.get_vacancies_with_keyword(name) ):
            print(f'{index+1} вакансия: {info[0]} ссылка: {info[1]} ')

print('меню\n',
      '0: выход\n',
      '1: получает список всех компаний и количество вакансий у каждой компании.\n',
      '2: получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.\n',
      '3: получает среднюю зарплату по вакансиям\n',
      '4: получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.\n',
      '5: получает список всех вакансий, в названии которых содержатся ключевое слово, например python.')
while True:
    try:
        user_answer = int(input().strip())
    except ValueError:
        print('пожалуйста введите число')
    else:
        if user_answer == 0:
            break
        dbmanager = DBManager()
        if user_answer == 1:
            print(dbmanager.print_companies_and_vacancies_count() )
        if user_answer == 2:
            print(dbmanager.print_all_vacancies()  )
        if user_answer == 3:
            print(f'средняя зп: {dbmanager.get_avg_salary()  }')
        if user_answer == 4:
            print(dbmanager.print_vacancies_with_higher_salary()  )
        if user_answer == 5:
            name=input('введите ключевое слово (регистр учитывается, если ничего не найдено попробуйте другой регистр)').strip()
            print(dbmanager.print_vacancies_with_keywor(name ))