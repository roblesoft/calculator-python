#encoding: utf-8
from utilstools import *
from funcalc import *
from groupingSings import *
import time
import os

def main():
    os.system('color F0')
    os.system('title CALC 1.4.5')
    while True:
        os.system('cls')
        print(introducing)
        op = menu()
        while op == '1' or op == 'y' or op == 'Y':
            os.system('cls')
            print(introducing)
            operation = str(input(">>>"))
            other = operation
            operation = replaceWhiteSpace(operation)
            operation = groupingSings(operation)
            operation = calculator(operation)
            os.system('cls')
            print(introducing)
            print('>>>', other, '=', operation)
            op = str(input('other operation? (Y/N)'))
            try:
                neverzero = float(operation) - int(float(operation))
                if neverzero == 0: operation = int(float(operation))
                else: operation = float(operation)
            except ValueError:
                continue
        if op =='2':
            pass
        if op =='3':
            os.system('cls')
            print(bye)
            time.sleep(.7)
            os.system('cls')
            break

if __name__ == '__main__':
    main()    
