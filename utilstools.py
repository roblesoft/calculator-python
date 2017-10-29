#encoding: utf-8
import os
import time
introducing ="""
 ╔═══════════════════════════════════════════════════════════════════════════╗
╔╝                   ░███████      ░█     ░█        ░███████ ©               ╚╗
║                   ░█      ░█    ░█░█    ░█       ░█      ░█                 ║
║ §                 ░█           ░█  ░█   ░█       ░█                       § ║
║                   ░█      ░█  ░█    ░█  ░█       ░█      ░█                 ║ 
╚╗                   ░███████  ░█      ░█ ░███████  ░███████  1.4.5          ╔╝
 ╚═══════════════════════════════════════════════════════════════════════════╝
                          «Desing by {brainet}®, 2017»

 """
bye = """
       _______  _______  _______  ______    _______  __   __  _______  __  
      |       ||       ||       ||      |  |  _    ||  | |  ||       ||  | 
      |    ___||   _   ||   _   ||  _    | | |_|   ||  |_|  ||    ___||  | 
      |   | __ |  | |  ||  | |  || | |   | |       ||       ||   |___ |  | 
      |   ||  ||  |_|  ||  |_|  || |_|   | |  _   | |_     _||    ___||__| 
      |   |_| ||       ||       ||       | | |_|   |  |   |  |   |___  __  
      |_______||_______||_______||______|  |_______|  |___|  |_______||__|                                                          
                      
"""
def gen(a,b):
    if a > b:
        a += 1
        while a != b:
            a -= 1
            yield a
    if a < b:        
        a -= 1
        while a != b:
            a += 1
            yield a        

def replaceWhiteSpace(string):
    string = ('  ' + string + '  ')
    return string

def menu():
    while True:
        print('\t\t\t\t    WELCOME!')
        print('\t\t\t\t1.- Calculator')
        print('\t\t\t\t2.- Functions')
        print('\t\t\t\t3.- Exit')
        choice = str(input('\t\t\t\t->'))
        if choice == '1':
            return choice
        elif choice == '2':
            return choice
        elif choice == '3':
            return choice
        else:
            print('\t\t\t\t other choice')
            time.sleep(0.5)
            os.system('cls')
            print(introducing)

