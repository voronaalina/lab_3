#в основі прямої призми лежить прямокутний трикутник. Користувач задає катети цього трикутника і висоту призми. Обчисліть іі об'єм.

import sys
if(len(sys.argv)!=4):
    print("error")
else:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    h = float(sys.argv[3])
    v = 0.5*a*b*h
    print("Об'єм призми=:",v)