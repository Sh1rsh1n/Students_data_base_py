from querys import crud
from sqlite3 import Error
from data_provider import user_input as us_in


def add():
    stdn = us_in.input_data()
    try:
        crud.exec_cud(crud.create, stdn)
        stdn_list = crud.get_all()
        print('\n')
    except Error:
        print('Что-то пошло не так... Возможно проблемы с БД.')


    print('=' * 50)
    print('||', 'фамилия'.center(10), '||', 'имя'.center(10), '||', 'класс '.center(10), ' ||')
    print('=' * 50)
    print('||', stdn_list[-1][1].center(10), '||', stdn_list[-1][2].center(10), '||', str(stdn_list[-1][0]).center(10),
          '||')
    print('=' * 50)
    print('||', "Ученик успешно добавлен.".center(10), '||')


def del_stdn():
    name = us_in.check_input_string('имя')
    surname = us_in.check_input_string('фамилия')
    class_desc = us_in.check_input_digit('класс', 1, 11)

    try:
        crud.exec_cud(crud.delete, (name, surname, class_desc))
    except Error:
        print('Что-то пошло не так... Возможно такой информации нет в БД.')

    print('=' * 50)
    print('||', 'фамилия'.center(10), '||', 'имя'.center(10), '||', 'класс '.center(10), ' ||')
    print('=' * 50)
    print('||', name.center(10), '||', surname.center(10), '||', str(class_desc).center(10),
          '||')
    print('=' * 50)
    print('||', "Ученик успешно удален.".center(10), '||')


def update_stdn():
    name = us_in.check_input_string('имя')
    surname = us_in.check_input_string('фамилия')
    class_desc = us_in.check_input_digit('класс', 1, 11)
    try:
        id = crud.get_id(name, surname, class_desc)
    except Error:
        print('Что-то пошло не так... Возможно такой информации нет в БД.')

    new_class_desc = us_in.check_input_digit('новый класс', 1, 11)
    age = us_in.check_input_digit('возраст', 7, 16)
    status = us_in.status('статус ученика')
    try:
        crud.exec_cud(crud.update, (new_class_desc, age, status, id))
    except Error:
        print('Что-то пошло не так... Возможно проблемы с БД.')

    print('=' * 72)
    print('||', 'фамилия'.center(10), '||', 'имя'.center(10), '||', 'класс '.center(10), ' ||')
    print('=' * 72)
    print('||', name.center(10), '||', surname.center(10), '||', str(new_class_desc).center(10),
          '||', age.center(10), '||', status.center(10), '||')
    print('=' * 72)
    print('||', "Данные о ученике успешно изменены.".center(10), '||')
