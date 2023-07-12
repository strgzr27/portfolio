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

print('Задача 9. Аннуитетный платёж')

def payment(summ, time, percent):
  k = (percent * (1 + percent) ** time) / ((1 + percent) ** time - 1)
  perayment = round(k * summ, 2)
  return perayment

def printout(summ, percent, perayment, time):
  for i in range(1, period + 1):
    paid_percent = summ * percent
    paid_credit = perayment - paid_percent
    print('\nПериод:', i)
    print('Остаток долга на начало периода:', summ)
    print('Выплачено процентов:', paid_percent)
    print('Выплачено тела кредита:', paid_credit)
    summ -= paid_credit
  else:
    print('\nОстаток долга', summ)
    return summ

credit = float(input('Введите сумму кредита: '))
time = int(input('На сколько лет выдан? '))
percent = int(input('Сколько процентов годовых? ')) / 100
period = 3 
A = payment(credit, time, percent)
balance = printout(credit, percent, A, time)
period = time - period

print('\n', '=' * 30)
time = int(input('\nНа сколько лет продляется договор? '))
period += time
percent = int(input('Увеличение ставки до: ')) / 100
A = payment(balance, period, percent)
balanse = printout(balance, percent, A, time)

# Кредит в сумме S млн руб.,
# выданный на n лет под i% годовых,
# подлежит погашению равными ежегодными выплатами в конце каждого года,
# включающими процентные платежи и сумму в погашение основного долга.
# Проценты начисляются в один раз в год.
# После выплаты третьего платежа
# достигнута договорённость между кредитором и заёмщиком
# о продлении срока погашения займа на n_2 лет
# и увеличении процентной ставки с момента конверсии до i_2%.
#
# Напишите программу,
# которая выводит план погашения оставшейся части долга.
# A = KS
# K = i(1 + i) ** n / (1 + i) ** n - 1
