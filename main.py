# Игра угадай число 
from random import randint

n = randint(1, 10)
k = input("Угадай целое число от 1 до 10: ")

while 1:
    if k == "Выход: ":
        print("В следующий раз повезет!")
        break
    k = int(k)
    
    if k == n:
        print("Ты угадал!")
        break
    
    print("Ваше число " + ("больше" if k > n else "меньше") + ", чем задумал компьютер")
    
k = input("Повтори попытку: ")
print("Загаданным числом было: " + str(n))
