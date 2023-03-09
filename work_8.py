import os
import random

# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# 1.чтение
# 2.поиск
# 3.добавить
# 4.сохранить

spraf_file = r'C:\Users\Леонид\home work 1\spraf.txt'

def append_spraf(spraf_file):
    spraf=input('Введите контакт в формате Ф И О Телефон:')
    with open(spraf_file,'a',encoding="utf-8") as f:
        f.write(f'\n{spraf}')
    print ('Контакт добавлен')    

def read_file(spraf_file):
    with open(spraf_file,'r',encoding="utf-8") as f:
        print (f.read())

def search_spraf (spraf_file):
    spraf_by=input("Введите информацию для поиска (фамилия,имя или отчество):")
    with open (spraf_file,'r',encoding="utf-8") as f:
        for line in f:
            if spraf_by in line:
                print(line) 

def delete(l):
    delete_param = (input('Введите контакт удаления: ' ).title())
    with open (file_path, 'w', encoding='utf8') as open_book:
        for line in l:
            if delete_param in line:
                print('Вы удалили контакт:', line)
            elif delete_param not in line:
               open_book.writelines(line)

def user_action():
    print('Добро пожаловать! 1)Ввести весь справочник 2)Добавить контакт 3) Найти контакт 4)Удалить контакт: ')
    while (input1:= int (input('Выберите действие со справочником (0=выход)='))) !=0:
        if input1 == 1:
            read_file(spraf_file)
        elif input1 == 2:
            append_spraf(spraf_file)
        elif input1 == 3:
            search_spraf (spraf_file)
        elif input1 == 4:
            del_str_spraf (spraf_file)
        else:
            print ("Ошибка") 

user_action()               


