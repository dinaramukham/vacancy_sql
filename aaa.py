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


