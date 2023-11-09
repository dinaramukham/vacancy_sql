from classes.wr_sql import  wr_sql
from classes.api import  HeadHunter


if __name__=='__main__':
    list_id=[15478, 3529, 1740, 4219, 4219, 41862, 3776, 733, 2180, 3127, 947]
    list_vacansies=[]
    for employer_id in list_id:
        vacansies= HeadHunter.get_json_info(employer_id=employer_id )
        for vacansy in vacansies:
            list_vacansies.append(HeadHunter.get_info(vacansy))
    for vacansy in list_vacansies:
        wr_sql(vacansy)



