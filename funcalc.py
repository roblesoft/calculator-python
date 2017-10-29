from utilstools import gen 
#encoding: utf-8
def calculator(string):
    all_digits = '0123456789.-'
    all_sings = '*/+~(){}[]'
    ind = 0
    indice = 0
    for i in string:
        if i == '*' or i == '/':
            for c in gen(ind -1, 0):
                if string[c] in all_sings:
                    break
                if string[c] in all_digits :
                    a = float(string[c:ind])
            for e in gen(ind + 1, len(string) - 1):
                if string[e] in all_sings:
                    break
                if string[e] in all_digits:
                    try:
                        b = float(string[ind + 1:e +1])
                    except ValueError:
                        continue
            if i == '*': result = float(a*b)
            else: result = float(a/b)
            result = str(result)
            string = string.replace(string[c+1:e], result)
            string = calculator(string)
            break
        indice += 1
        ind = indice

    c = 0
    e = 0
    ind = 0
    indice = 0
    for i in string:
        if i == '+' or i == '~':
            for c in gen(ind -1, 0):
                if string[c] in all_sings:
                    break
                if string[c] in all_digits:
                    a = float(string[c:ind])
            for e in gen(ind + 1, len(string) - 1):
                if string[e] in all_sings:
                    break
                if string[e] in all_digits:
                    try:
                        b = float(string[ind + 1:e +1])
                    except ValueError:
                        continue
            if i == '+': result = float(a + b)
            else : result = float(a-b)
            result = str(result)
            string  = string.replace(string[c + 1:e], result)
            string = calculator(string)
            break
        indice += 1
        ind = indice
    return string
