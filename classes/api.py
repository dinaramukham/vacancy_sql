import requests

class HeadHunter:
    """
    для получения инфы с hh.ru
    """
    @classmethod
    def get_json_info(cls, employer_id=None ):
        """
        возвращыет словарь json с инфой, каждый элемент вакансия employer_id компания
        """
        params = {'page': 0, 'employer_id': employer_id,
                  'per_page': 100}
        url = 'https://api.hh.ru/vacancies'

        list_info = []
        try:
            for num in range(0, 1):  # максимум 2000 экземпляров это до 20
                params['page'] = num
                html_text = requests.get(url, params).json()
                for number in range(0, 100):
                    list_info.append(html_text['items'][number])
            return list_info
        except IndexError:
            return list_info
    @classmethod
    def get_info(cls, data):  # млжет словарь
        dict_={}
        dict_['name']=data['name'] # название вакансии
        dict_['company_name'] = data['employer']['name']
        dict_['url']=data['alternate_url'] # ссылка
        if data['salary'] != None :
            dict_['from'] = data['salary'].get('from')
            dict_['to'] = data['salary'].get('to')
            dict_['currency'] = data['salary'].get('currency')
        else:
            dict_['from'] = None
            dict_['to'] = None
            dict_['currency'] = None
        if data['address'] != None :
            dict_['address']=  data['address']['raw'] # адрес 'raw'
        else:
            dict_['address'] = None
        dict_['responsibility']=data['snippet']['responsibility'] # обязаности
        dict_['requirement']=data['snippet']['requirement'] # требования
        return dict_

#название вакансии ссылка зп обязаности требования опыт работы адрес регион
#for index, value in enumerate(HeadHunter.get_json_info()) :
#    print(value['address']  )  # 'alternate_url'
# ---15478 вк----3529 сбер----1740 яндекс----4219 теле2----41862 скб контур----3776 мтс диджитал----733 ланит----2180 озон----3127 мегафон----947 данон
#data=HeadHunter.get_json_info(employer_id= 1740)
#print(type(data) )
#for el in data:
#    print(el['employer']['name']    )