#!/bin/env python3
from random import randrange,choice
from sys import argv

# Config
especial=True
MAXLENGTH=42
MINLENGTH=12

def geratePassWord(length:int=MINLENGTH,especial:bool=True):
    if length<MINLENGTH or length>MAXLENGTH:
        raise Exception(f"Tamanho da senha fora do limite\nMinimo:{MINLENGTH} - Maximo:{MAXLENGTH}")

    stringASCII=(48,57)
    intASCII=(97,122)
    especialASCI=[33,35,36,37,38,95]
    password=''
    if especial:
        choicesList=[stringASCII,intASCII,especialASCI]
    else:
        choicesList=[stringASCII,intASCII]
    for count in range(length):
        selected=choice(choicesList)
        if(type(selected)==type([])):
            password+=chr(choice(selected))
        elif (type(selected)==type("")):
            string=(chr(randrange(selected[0],selected[1])))
            if(choice([True,False])): 
                string=str.upper(string)
            password+=string
        else:
            password+=str(chr(randrange(selected[0],selected[1])))
    return password

if (len(argv)>1):
    
    try:
        if argv[2] == "--no-especial":
            especial=False
    except:
        pass
    try:
        print(geratePassWord(length=int(argv[1]),especial=especial))
    except ValueError:
        print('O tamanho da senha tem que ser numerico')
    except Exception as error:
        print(error.args[0])
else:
    print(geratePassWord())
