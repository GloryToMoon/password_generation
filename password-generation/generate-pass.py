#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys

pass_db_int=[]
pass_db_str=[]

def read_file(input):
    global pass_db, pass_db_int, pass_db_str
    file = open(input,"r")
    pass_db=file.read().split("\n")
    pass_db.remove("")
    file.close()

def sort_patterns():
    ## Переворачиваем цифровые шаблоны
    for string in pass_db:
        if string.isdigit() == True:
            if string[::-1] != string:
                pass_db_int.append(string[::-1])
            pass_db_int.append(string)
    ## И строки
        if string.isdigit() == False:
            if string[::-1] != string:
                pass_db_str.append(string[::-1])
            pass_db_str.append(string)

def generate_passwords():
    ## Добавляем к финальному списку строковые шаблоны
    for str_i in pass_db_str:
        pass_db.append(str_i)
        pass_db.append(str_i.upper())
        pass_db.append(str_i.title())

    ## То же, но с числовыми
    for int_i in pass_db_int:
        pass_db.append(int_i)
    ## Добавляем шаблоны <строка>+<число> и наоборот
        for str_i in pass_db_str:
            pass_db.append(str_i + int_i)
            pass_db.append(int_i + str_i)
            pass_db.append(str_i + "_" + int_i)
            pass_db.append(int_i + "_" + str_i)
            pass_db.append(str_i + " " + int_i)
            pass_db.append(int_i + " " + str_i)
            pass_db.append(str_i + "-" + int_i)
            pass_db.append(int_i + "-" + str_i)

def check():
    global pass_db
    pass_db = list(set(pass_db))

def write_file(output):
    ## Финальный результат
    print ('\033[32;1m' + 'Total passwords: ' + '\033[37;1m' +str(len(pass_db)))
    output_file = open ('out-' + output,"w")
    for i in pass_db:
        output_file.write (i + '\n')
    output_file.close()

if __name__ == '__main__':
    if len (sys.argv) == 2:
        read_file(sys.argv[1])
        sort_patterns()
        check()
        generate_passwords()
        check()
        write_file(sys.argv[1])
    else:
        print ("Usage: python3 generate-pass.txt input.txt")
