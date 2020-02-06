#Задачи на циклы и оператор условия
'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
print( "Задача 1. Цикл while")
i = 1
while i <= 5:
    print(i, "00000")
    i +=1

print("Задача 1. Цикл for")
for i in range(1, 6):
    print(i, "00000")

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
print("Задача 2. Цикл while")
n = 0
i = 0
while i < 10:
    number = int(input("Введите цифру"))
    if number == 5:
        n += 1
        i += 1
    else:
        i += 1
print("Введено пятёрок", n)

print("Задача 2. Цикл for")
n = 0
for i in range(10):
    number = int(input("Введите цифру"))
    if number == 5:
        n += 1
print("Введено пятёрок", n)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
print("Задача 3. Цикл while")
sum = 0
i = 0
while i <= 100:
    sum +=i
    i +=1
print (sum)

print( "Задача 3. Цикл for")
sum = 0
for i in range(1,101):
    sum+=i
print(sum)

print( "Задача 3. Проверка")
print(1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20+21+22+23+24+25+26+27+28+29+30+31+32+33+34+35+36+37+38+39+40+41+42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62+63+64+65+66+67+68+69+70+71+72+73+74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
print("Задача 4. Цикл while")
product = 1
i = 1
while i <= 10:
    product *=i
    i +=1
print (product)

print( "Задача 4. Цикл for")
product = 1
for i in range(1,11):
    product *=i
print(product)

print( "Задача 4. Проверка")
print(1*2*3*4*5*6*7*8*9*10)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
print("Задача 5. Цикл while. Обратный порядок")
integer_number = 2129
#print(integer_number%10,integer_number//10)
while integer_number>0:
    print(integer_number%10)
    integer_number = integer_number//10

print("Задача 5. Цикл for. Прямой порядок")
integer_number = 2129
integer_number = str(integer_number)
for i in range(0, len(integer_number)):
    print(integer_number[i])

'''
Задача 6
Найти сумму цифр числа.
'''
print("Задача 6. Цикл while")
number = 123456
sum = 0
while number>0:
    sum += number%10
    number = number//10
print(sum)

print("Задача 6. Цикл for")
number = str(123456)
sum = 0
for i in range(len(number)):
    sum += int(number[i])
print(sum)

print("Задача 6. Проверка")
print(1+2+3+4+5+6)
'''
Задача 7
Найти произведение цифр числа.
'''
print("Задача 7. Цикл while")
number = 123456
product = 1
while number>0:
    product *= number%10
    number = number//10
print(product)

print("Задача 7. Цикл for")
number = str(123456)
product = 1
for i in range(len(number)):
    product *= int(number[i])
print(product)

print("Задача 7. Проверка")
print(1*2*3*4*5*6)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
print("Задача 8. Цикл while")
integer_number = 123456
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else:
    print('No')

print("Задача 8. Цикл for")
answer = 'No'
integer_number = str(123456)
for i in range(len(integer_number)):
    if integer_number[i] == "5":
        answer = 'Yes'
        break
print(answer)
'''
Задача 9
Найти максимальную цифру в числе
'''
print("Задача 9. Цикл while")
number = 17234568
i = 0
max = int(str(number)[0])
while i < len(str(number)):
    if max >= int(str(number)[i]):
        i += 1
        continue
    else:
        max = int(str(number)[i])
        i += 1
print(max)

print("Задача 9. Цикл for")
number = 17234568
max = int(str(number)[0])
for i in range(len(str(number))):
    if int(str(number)[i]) > max:
        max = int(str(number)[i])
    else:
        continue
print(max)

'''
Задача 10
Найти количество цифр 5 в числе
'''
print("Задача 10. Цикл while")
number = 1235545655789
n = 0
i = 0
while i < len(str(number)):
    if int(str(number)[i]) == 5:
        n +=1
    i += 1
print(n)

print("Задача 10. Цикл for")
number = 12345655789
n = 0
for i in str(number):
    if int(i) == 5:
        n += 1
    else:
        continue
print(n)
