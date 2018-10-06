import math
import time
while True:
	num = input("Напиши любой знак вычисления, если значение будет равно нулю процесс завершится(+, -, /, *, //, **, sqrt(корень), sin, cos, tan, hypot: ")
	if num == ("0"):
		print ("Процесс завершится через 3 секунд")
		time.sleep(3)
		break
	if num in ("+, -, /, *, //, **, sqrt, sin, cos, tan, hypot"):
		if num == '+':
			x = float(input("Первое число= "))
			y = float(input("Второе число= "))
			print((x+y))
		elif num == '-':
			x = float(input("Первое число= "))
			y = float(input("Второе число= "))
			print((x-y))
		elif num == '*':
			x = float(input("Первое число= "))
			y = float(input("Второе число= "))
			print((x*y))
		elif num == '/':
			x = float(input("Первое число= "))
			y = float(input("Второе число= "))
			try:
				print((x/y))
			except ZeroDivisionError:
				print("Вот ты скажи мне, нафига делить на ноль, А?!")
		elif num == '//':
			x = float(input("Первое число= "))
			y = float(input("Второе число= "))
			try:
				print((x//y))
				print((x%y))
			except ZeroDivisionError:
				print("Деление на ноль!")
		elif num == '**':
			x = float(input("Первое число= "))
			y = float(input("Второе число= "))
			print((x**y))
		elif num == 'sqrt':
			try:
				x = float(input("Число из которого будет браться корень: "))
				y = 0
				print((math.sqrt(x)))
			except ZeroDivisionError:
				print("Деление на ноль!")
		elif num == 'sin':
			try:
				x = float(input("A: "))
				print((math.sin(x)))
			except ValueError:
				print("Не обманывай меня, я крутой искусственный интелект!")
		elif num == 'cos':
			try:
				x = float(input("A: "))
				print((math.cos(x)))
			except ValueError:
				print("Не обманывай меня, я крутой искусственный интелект!")
		elif num == 'tan':
			try:
				x = float(input("A: "))			
				print((math.tan(x)))
			except ValueError:
				print("Не обманывай меня, я крутой искусственный интелект!")
		elif num == 'hypot':
			try:
				x = float(input("A: "))
				y = float(input("B: "))
				print((math.hypot(x, y)))
			except ValueError:
				print("Не обманывай меня, я крутой искусственный интелект!")
	else:
		print("Неправильное значение!")