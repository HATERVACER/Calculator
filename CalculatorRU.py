#Модули которые будут импортированы
#Математический модуль для корней, синусов, косинусов, тангенсов. 
import math
#Время для выхода
import time
#Цикл
while True:
	#Первая строка которая будет выведена
	num = input("Напиши любой знак вычисления, если значение будет равно нулю процесс завершится(+, -, /, *, //, **, sqrt(корень), sin, cos, tan, hypot: ")
	#Выход
	f num == ("0"):
		print ("Процесс завершится через 3 секунд")
		time.sleep(3)
		break
	#Проверка операций
	if num in ("+, -, /, *, //, **, sqrt, sin, cos, tan, hypot"):
		#Первая операция(+)
		if num == '+':
			x = float(input("Первое число= "))
			y = float(input("Второе число= "))
			print((x+y))
		#Вторая операция(-)
		elif num == '-':
			x = float(input("Первое число= "))
			y = float(input("Второе число= "))
			print((x-y))
		#Третья операция(умножение)
		elif num == '*':
			x = float(input("Первое число= "))
			y = float(input("Второе число= "))
			print((x*y))
		#Четвертая
		elif num == '/':
			x = float(input("Первое число= "))
			y = float(input("Второе число= "))
			#Проверка на ошибки в написании
			try:
				print((x/y))
			except ZeroDivisionError:
				print("Вот ты скажи мне, нафига делить на ноль, А?!")
		#Деление с остатком
		elif num == '//':
			x = float(input("Первое число= "))
			y = float(input("Второе число= "))
			try:
				print((x//y))
				print((x%y))
			except ZeroDivisionError:
				print("Деление на ноль!")
		#Степень
		elif num == '**':
			x = float(input("Первое число= "))
			y = float(input("Второе число= "))
			print((x**y))
		#Корень
		elif num == 'sqrt':
			try:
				x = float(input("Число из которого будет браться корень: "))
				y = 0
				print((math.sqrt(x)))
			except ZeroDivisionError:
				print("Деление на ноль!")
		#Синус
		elif num == 'sin':
			try:
				x = float(input("A: "))
				print((math.sin(x)))
			except ValueError:
				print("Не обманывай меня, я крутой искусственный интелект!")
		#Косинус
		elif num == 'cos':
			try:
				x = float(input("A: "))
				print((math.cos(x)))
			#Проверка на буквы
			except ValueError:
				print("Не обманывай меня, я крутой искусственный интелект!")
		#Тангенс
		elif num == 'tan':
			try:
				x = float(input("A: "))			
				print((math.tan(x)))
			except ValueError:
				print("Не обманывай меня, я крутой искусственный интелект!")
		#Гипотенуза
		elif num == 'hypot':
			try:
				x = float(input("A: "))
				y = float(input("B: "))
				print((math.hypot(x, y)))
			except ValueError:
				print("Не обманывай меня, я крутой искусственный интелект!")
	#Произойдет если в num не будет значения операции 
	else:
		print("Неправильное значение!")
