from utilstools import gen, replaceWhiteSpace
from funcalc import *

def groupingSings(string):
    for i in gen(0, (len(string) - 1)):
        if string[i] == '(':
            for j in gen(i, (len(string) -1)):
                if string[j] == ')':
                    new_string = string[i+1:j]
                    new_string = replaceWhiteSpace(new_string)
                    new_string = calculator(new_string)
                    string = string.replace(string[i:j + 1], new_string)
                    break
            break
        
    for i in gen(0, (len(string) - 1)):
        if string[i] == '[':
            for j in gen(i, (len(string) -1)):
                if string[j] == ']':
                    new_string = string[i+1:j]
                    new_string = replaceWhiteSpace(new_string)
                    new_string = calculator(new_string)
                    string = string.replace(string[i:j + 1], new_string) 
                    break
            break
        
    for i in gen(0, (len(string) - 1)):
        if string[i] == '{':
            for j in gen(i, (len(string) -1)):
                if string[j] == '}':
                    new_string = string[i+1:j]
                    new_string = replaceWhiteSpace(new_string)
                    new_string = calculator(new_string)
                    string = string.replace(string[i:j + 1], new_string)
                    break
            break
        
    return string
