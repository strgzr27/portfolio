#оператор_if#

print('Прогрессивный налог')
income = int(input('Введите величину дохода: '))
if income < 10000:
  tax = income * 0.13
elif income < 50000:
  tax = (income - 10000) * 0.2 + 10000 * 0.13
else:
  tax = (income - 50000) * 0.3 + (50000 - 10000) * 0.2 + 10000 * 0.13
print('Сумма налога:', tax)

#Циклы#
print('Счастливый билетик')
number = int(input('Введите шестизначный номер билета: '))
left_sum = 0
right_sum = 0
count = 0
while count < 3:
  last_num = number % 10
  print(last_num)
  right_sum += last_num
  number //= 10
  count += 1
print('сумма справа:',right_sum)
while count < 6:
  last_num = number % 10
  print(last_num)
  left_sum += last_num
  number //= 10
  count += 1
print('сумма слева:',left_sum)
if left_sum == right_sum:
  print('Билет счастливый!')
else:
  print('Билет не счастливый')

###
print('Игра «Компьютер угадывает число»')
print()
print('Загадайте число от 1 до 100 включительно.')
min = 0
max = 100
count = 0
N = 50
while True:
  print('Твое число равно(1), больше(2) или меньше(3), чем число', int(N),'?')
  count += 1
  Try = int(input('Введите ответ 1/2/3: '))
  if Try == 1:
    print('Компьютер угадал! Количество попыток:', count)
    break
  elif Try == 2:
    min = N
    N += (max - min) / 2
    if N % 1 != 0:
      N += 0.5
  elif Try == 3:
    max = N
    N -= (max - min) / 2
    if N % 1 != 0:
      N += 0.5
  else:
    print('Ошибка! Введите ответ 1/2/3')

#Вложенные циклы
print('Задача. Яма')
N = int(input('Введите число: '))
print()
for row in range(N):
  for col in range(N*2):
    if col <= row:
      print(N-col, end = '')
    elif col >= N*2-row-1:
      print(col-N+1, end = '')
    else:
      print('.', end = '')
  print()

#Функции

def rock_paper_scissors(choice):
  sign = input('Введите - камень, ножницы или бумага: ')
  if sign == "ножницы":
    print('Вы выйграли! У меня - "бумага".')
  elif sign == 'бумага':
    print('Ничья! У меня тоже "бумага"')
  elif sign == 'камень':
    print('Я победил! У меня "бумага"')
  input('Введите любую цифру для возврата в меню: ')
  mainMenu()
  
def guess_the_number(choice):
  while True:
    number = int(input('Введите число: '))
    if number == 7:
      print('Вы угадали!')
      break
    else:
      print('Вы не угадали.')
  input('Введите любой символ для возврата в меню: ')
  mainMenu()

def mainMenu():
  choice = int(input('Выберите игру! 1 - «Камень, ножницы, бумага», 2 - «Угадай число»: '))
  if choice == 1:
    rock_paper_scissors(choice)
  if choice == 2:
    guess_the_number(choice)

mainMenu()


# Списки
N = int(input('Кол-во чисел в списке: '))
numbers_list = []
summ = 0
for i in range(N):
  print('Введите', i + 1, 'число: ', end = '')
  number = int(input(''))
  numbers_list.append(number)
K = int(input('\nВведите делитель: '))
print()
for id in range(N):
  if numbers_list[id] % K == 0:
    print('Индекс числа', numbers_list[id], end = '')
    print(':', id)
    summ += id
print('Сумма индексов:', summ)

# Пользователь вводит список из N чисел и число K. Напишите код, выводящий на экран сумму индексов элементов списка, которые кратны K.
