#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def read_file(input):
    file = open(input,"r")
    pass_db=file.read().split("\n")[:-1]
    file.close()
    return pass_db

def sort_patterns(pass_db):
    pass_db_int=[]
    pass_db_str=[]
    for string in pass_db:
        ## Reverse numeric patterns
        if string.isdigit() == True:
            if string[::-1] != string:
                pass_db_int.append(string[::-1])
            pass_db_int.append(string)
        ## And Strings
        if string.isdigit() == False:
            if string[::-1] != string:
		## Add strings with upper words
                pass_db_str.append(string[::-1].upper())
                pass_db_str.append(string[::-1].title())
            pass_db_str.append(string.upper())
            pass_db_str.append(string.title())
    return pass_db_str, pass_db_int

def generate_passwords(pass_db,pass_db_int,pass_db_str):
    ## Add string patterns to final result
    for str_i in pass_db_str:
        pass_db.append(str_i)
    ## Same, but with numeric patterns
    for int_i in pass_db_int:
        pass_db.append(int_i)
    ## Add patterns like <string>+<number> and backward
        for str_i in pass_db_str:
            pass_db.append(str_i + int_i)
            pass_db.append(int_i + str_i)
            pass_db.append(str_i + "_" + int_i)
            pass_db.append(int_i + "_" + str_i)
            pass_db.append(str_i + " " + int_i)
            pass_db.append(int_i + " " + str_i)
            pass_db.append(str_i + "-" + int_i)
            pass_db.append(int_i + "-" + str_i)
    return pass_db

def check():
    global pass_db
    pass_db = list(set(pass_db))

def write_file(output,pass_db):
    ## Final result
    print ('\033[32;1m' + 'Total passwords: ' + '\033[37;1m' +str(len(pass_db)))
    output_file = open ('out-' + output,"w")
    for i in pass_db:
        output_file.write (i + '\n')
    output_file.close()

if __name__ == '__main__':
    if len (sys.argv) != 2:
        print ("Usage: python3 generate-pass.py patterns.txt")
        sys.exit(0)
    pass_db=read_file(sys.argv[1])
    pass_db_str,pass_db_int=sort_patterns(pass_db)
    pass_db=generate_passwords(pass_db,pass_db_int,pass_db_str)
    pass_db=list(set(pass_db))
    write_file(sys.argv[1],pass_db)
