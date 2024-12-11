"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.

Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела

Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.

Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.

13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]
def get_employers_data(department):
    list_empl_data = [x.get("employers") for x in departments if x.get("title") == department]
    return list_empl_data[0]

def task_level_1():
    #1
    departs = [x.get("title") for x in departments if x.get("title") is not None]
    print(f"№1 - {departs}")
    #2
    empl_names = list()
    for dep in departs:
        empls = get_employers_data(dep)
        empl_names.extend([x.get("first_name") + " "+ x.get("last_name") for x in empls])
    print(f"№2 - {empl_names}")    
    #3
    names_dep = list()
    for dep in departs:
        empls = get_employers_data(dep)
        names_dep.extend([x.get("first_name") + " "+ x.get("last_name") + " - " + dep for x in empls])
    print(f"№3 - {names_dep}")
    #4
    empl_names_100 = list()
    for dep in departs:
        empls = get_employers_data(dep)
        empl_names_100.extend([x.get("first_name") + " "+ x.get("last_name") for x in empls if x.get("salary_rub") > 100000])
    print(f"№4 - {empl_names_100}")  
    #5
    empl_position = list()
    empl_position_s = set()
    for dep in departs:
        empls = get_employers_data(dep)
        positions = [x.get("position") for x in empls if x.get("salary_rub") < 80000]
        empl_position.extend(positions)
        #без повторений(можно так же и без set просто if добавить на проверку есть ли элемент или нет перед добавлением)
        for el in positions:
            empl_position_s.add(el)
    print(f"№5 - {empl_position}, без повторений {empl_position_s}") 
    #6

    dep_money = list()
    for dep in departs:
        empls = get_employers_data(dep)
        summ_month = sum(x.get("salary_rub") for x in empls)
        dep_money.append(dep + ": сумма в месяц = " + str(summ_month) )
    print(f"№6 - {dep_money}")  

def task_level_2():
    #7
    departs = [x.get("title") for x in departments if x.get("title") is not None]
    dep_name_min_salary = list()
    for dep in departs:
        empls = get_employers_data(dep)
        min_salary = min(x.get("salary_rub") for x in empls)
        dep_name_min_salary.append(dep + ": min salaty = " + str(min_salary))
    print(f"№7 - {dep_name_min_salary}")
    #8
    dep_name_salarys = list()
    for dep in departs:
        empls = get_employers_data(dep)
        min_salary = min(x.get("salary_rub") for x in empls)
        avg_salary = sum(x.get("salary_rub") for x in empls) / len(empls)
        max_salary = max(x.get("salary_rub") for x in empls)
        dep_name_salarys.append(dep + ": min salary = " + str(min_salary) + ": avg salary = " 
                                + str(avg_salary) + ": max salary = " + str(max_salary))
    print(f"№8 - {dep_name_salarys}")   
    #9
    avg_salary = 0
    salarys = 0
    count_empl = 0
    for dep in departs:
        empls = get_employers_data(dep)
        count_empl += len(empls)
        salarys += sum(x.get("salary_rub") for x in empls)
    print(f"№9 - {salarys / count_empl}")
    #10
    empl_position_s = set()
    for dep in departs:
        empls = get_employers_data(dep)
        positions = [x.get("position") for x in empls if x.get("salary_rub") > 90000]
        for el in positions:
            empl_position_s.add(el)
    print(f"№10 - {empl_position_s}") 
    #11
    women = {"Michelle", "Nicole", "Christina", "Caitlin"}
    dep_avg_w_salary = list()
    empl_position_s = set()
    for dep in departs:
        empls = get_employers_data(dep)
        count_women = len([x for x in empls if x.get("first_name") in women])
        avg_salary = round(sum(x.get("salary_rub") for x in empls if x.get("first_name") in women) / count_women,2)
        dep_avg_w_salary.append(dep+ " - avg salary = " +str(avg_salary))
    print(f"№11 - {dep_avg_w_salary}") 
    #12
    vowel = "aeiouAEIOU"
    empl_names = list()
    for dep in departs:
        empls = get_employers_data(dep)
        empl_names.extend([x.get("first_name") for x in empls if x.get("last_name")[-1] in vowel])
    print(f"№12 - {empl_names}")   


def task_level_3():
    #13
    departs = [x.get("title") for x in departments if x.get("title") is not None]
    dep_avg_taxes = list()
    for dep in departs:
        empls = get_employers_data(dep)
        percent = [x.get("value_percents") for x in taxes if x.get("department") == dep]
        if percent == []:
            percent = [x.get("value_percents") for x in taxes if x.get("department") is None][0]
        else:
            percent = percent[0]
        avg_taxes = sum(x.get("salary_rub") * percent / 100 for x in empls) / len(empls)    
        dep_avg_taxes.append(dep + ": avg taxes = " + str(avg_taxes))
    print(f"№13 - {dep_avg_taxes}")
    #14
    empl_net = list()
    for dep in departs:
        empls = get_employers_data(dep)
        percent = [x.get("value_percents") for x in taxes if x.get("department") == dep]
        if percent == []:
            percent = [x.get("value_percents") for x in taxes if x.get("department") is None][0]
        else:
            percent = percent[0]
        empl_net.extend([x.get("first_name") + " " + x.get("last_name") + " зп на руки = " 
                         + str(x.get("salary_rub") - x.get("salary_rub") * percent / 100) for x in empls])
    print(f"№14 - {empl_net}")  
    #15 
    dep_sum_taxes = list()
    for dep in departs:
        empls = get_employers_data(dep)
        percent = [x.get("value_percents") for x in taxes if x.get("department") == dep]
        if percent == []:
            percent = [x.get("value_percents") for x in taxes if x.get("department") is None][0]
        else:
            percent = percent[0]
        sum_taxes = sum(x.get("salary_rub") * percent / 100 for x in empls)   
        dep_sum_taxes.append([dep, sum_taxes])
    sort_dep_sum_taxes = sorted(dep_sum_taxes, key = lambda x: x[1])
    print(f"№15 - {[dep[0] for dep in sort_dep_sum_taxes]}")
    #16
    empl_tax_year_100 = list()
    for dep in departs:
        empls = get_employers_data(dep)
        percent = [x.get("value_percents") for x in taxes if x.get("department") == dep]
        if percent == []:
            percent = [x.get("value_percents") for x in taxes if x.get("department") is None][0]
        else:
            percent = percent[0]
        empl_tax_year_100.extend([x.get("first_name") + " " + x.get("last_name") for x in empls 
                                  if 12*x.get("salary_rub") * percent / 100 >100000])
    print(f"№16 - {empl_tax_year_100}")  
    #17
    min_tax = float("inf") 
    empl_min_tax = ""
    for dep in departs:
        empls = get_employers_data(dep)
        percent = [x.get("value_percents") for x in taxes if x.get("department") == dep]
        if percent == []:
            percent = [x.get("value_percents") for x in taxes if x.get("department") is None][0]
        else:
            percent = percent[0]
        for el in empls:
            tax = el.get("salary_rub") * percent / 100
            if tax < min_tax:
                min_tax = tax
                empl_min_tax = el.get("first_name") + " " + el.get("last_name")
    print(f"№17 - {empl_min_tax}")  
    

def main():
    task_level_1()
    task_level_2()
    task_level_3()


if __name__ == "__main__":
    main()




