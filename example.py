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

def bedroom():
  print('Вы в спальне. Куда идем?')
  print('1 - в ванну')
  print('2 - в коридор')
  bedroom = int(input())
  if bedroom == 1:
    bath()
  elif bedroom == 2:
    corridor()

def corridor():
  print('Вы в коридоре. Куда идем?')
  print('1 - в спальню')
  print('2 - в ванну')
  print('3 - на кухню')
  print('4 - в дверь')
  corridor = int(input())
  if corridor == 1:
    bedroom()
  elif corridor == 2:
    bath()
  elif corridor == 3:
    kitchen()
  elif corridor == 4:
    door()

def bath():
  print('Вы в ванной. Куда идем?')
  print('1 - в спальню')
  print('2 - в коридор')
  bath = int(input())
  if bath == 1:
    bedroom()
  elif bath == 2:
    corridor()

def kitchen():
  print('Вы на кухне. Куда идем?')
  print('1 - в окно')
  print('2 - в коридор')
  kitchen = int(input())
  if kitchen == 1:
    window()
  elif kitchen == 2:
    corridor()

def window():
  print('Игрок вышел из окна и разбился. Игра окончена.')

def door():
  print('Игрок вышел наружу. Добро пожаловать в открытый мир!')

corridor()
