from classes.wr_sql import  wr_sql, wr_emp_sql,  create_sql
from classes.api import  HeadHunter
from classes.dbm_anager import  DBManager

if __name__=='__main__':
    list_id=[15478, 3529, 1740, 4219, 4219, 41862, 3776, 733, 2180, 3127, 947]
    create_sql()
    print('база данных "vacancies" на sql создана')

    list_vacansies=[]
    for employer_id in list_id:
        vacansies= HeadHunter.get_json_info(employer_id=employer_id )
        for vacansy in vacansies:
            list_vacansies.append(HeadHunter.get_info(vacansy))
    print('вакансии с hh.ru получены')

    for index, vacansy in enumerate(list_vacansies):
        try:
            if vacansy['company_name'] != list_vacansies[index+1]['company_name']:
                wr_emp_sql(vacansy)
        except IndexError:
            break
    wr_emp_sql(list_vacansies[-1])
    for vacansy in list_vacansies:
        wr_sql(vacansy)
    print('вакансии и компании в таблицы "vacancies" "employers" сохранены')

    print('меню\n',
          '0: выход\n',
          '1: получить список всех компаний и количество вакансий у каждой компании.\n',
          '2: получить список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.\n',
          '3: получить среднюю зарплату по вакансиям\n',
          '4: получить список всех вакансий, у которых зарплата выше средней по всем вакансиям.\n',
          '5: получить список всех вакансий, в названии которых содержатся ключевое слово, например python.')
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
                print(dbmanager.print_companies_and_vacancies_count())
            if user_answer == 2:
                print(dbmanager.print_all_vacancies())
            if user_answer == 3:
                print(f'средняя зп: {dbmanager.get_avg_salary()}')
            if user_answer == 4:
                print(dbmanager.print_vacancies_with_higher_salary())
            if user_answer == 5:
                name = input(
                    'введите ключевое слово (регистр учитывается, если ничего не найдено попробуйте другой регистр)').strip()
                print(dbmanager.print_vacancies_with_keywor(name))


