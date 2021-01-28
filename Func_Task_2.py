def person(name, first_name, email, tel, year, city):
    print_pers = 'ФИО. {} {} Родились в {} года. Проживаете в городе {}. Ваша почта. {}, тел. {} '.format(name,
                                                                                                          first_name,
                                                                                                          year, city,
                                                                                                          email, tel)
    return print_pers


try:
    print(person(name=input('Имя: ').lower().title(), first_name=input('Фамиля: ').lower().title(),
                 year=int(input("Год рождения: ")),
                 city=input('Город проживания: ').lower().title(),
                 email=input('Ваш email: ').lower(), tel=int(input('Тел: '))))
except ValueError:
    print('Вы ввели не число')
