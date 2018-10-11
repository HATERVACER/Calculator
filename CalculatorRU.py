#Модули которые будут импортированы
#Математический модуль для корней, синусов, косинусов, тангенсов. 
import math
#Время для выхода
import time
#Цикл
while True:
	#Первая строка которая будет выведена 
	print('Напиши любой знак вычисления, если значение будет равно нулю процесс завершится(+, -, /, *, //, **, sqrt(корень), sin, cos, tan, hypot, log, log1p, log10, log2, degress, radians, asin, acon, atan, atan2, sinh, cosh, tanh, asinh, acosh, ')	
	num = input("atanh, gamma, lgamma, Scircle(Площадь круга), Ssquad(Площадь квадрата), S(Площадь), Pcircle(Периметр круга, P(Периметр прямоугольника), Psquad(Периметр квадрата)): ")
	#Выход
	if num == ("0"):
		print ("Процесс завершится через 3 секунды")
		time.sleep(3)
		break
	#Проверка операций
	if num in ("+, -, /, *, //, **, sqrt, sin, cos, tan, hypot, log, log1p, log10, log2, degress, radians, asin, acon, atan, atan2, sinh, cosh, tanh, asinh, acosh, atanh, gamma, lgamma, Scircle, Ssquad, S, Pcircle, P, Psquad"):
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
		# Логарифмирование
		elif num == 'log':
			a = float(input("Число: "))
			print(math.log(a))
		# Натуральное логарифмирование
		elif num == 'log1p':
			a = float(input("Число: "))
			print(math.log1p(a))
		# Логарифм A по основанию 10
		elif num == 'log10':
			a = float(input("Число: "))
			print(math.log10(a))
		# Логарифм A по основанию 2
		elif num == 'log2':
			a = float(input("Число: "))
			print(math.log2(a))
		# Конвертирует радианы в градусы
		elif num == 'degress':
			a = float(input("Радианы: "))
			print(math.degrees(a))
		# Конвертирует градусы в радианы
		elif num == 'radians':
			a = float(input("Градусы: "))
			print(math.radians(a))
		# Арксинус в радианах
		elif num == 'asin':
			a = float(input("A: "))
			print(math.asin(a))
		# Арккосинус в радианах
		elif num == 'acos':
			a = float(input("A: "))
			print(math.acos(a))
		# Арктангенс в радианах
		elif num == 'atan':
			a = float(input("A: "))
			print(math.atan(a))
		# Арктангенс в радианах, с учетом четверти, в которой находится точка
		elif num == 'atan2':
			a = float(input("A: "))
			b = float(input("B: "))
			print(math.atan2(a, b))
		# Вычесляет гиперболический синус
		elif num == 'sinh':
			a = float(input("A: "))
			print(math.sinh(a))
		# Вычесляет гиперболический косинус
		elif num == 'cosh':
			a = float(input("A: "))
			print(math.cosh(a))
		# Вычесляет гиперболический тангенс
		elif num == 'tanh':
			a = float(input("A: "))
			print(math.tanh(a))
		# Вычесляет обратный гиперболический синус
		elif num == 'asinh':
			a = float(input("A: "))
			print(math.asinh(a))
		# Вычесляет обратный гиперболический косинус
		elif num == 'acosh':
			a = float(input("A: "))
			print(math.acosh(a))
		# Вычесляет обратный гиперболический тангенс
		elif num == 'atanh':
			a = float(input("A: "))
			print(math.atanh(a))
		# Гамма-функция
		elif num == 'gamma':
			a = float(input("A: "))
			print(math.gamma(a))
		# Натуральный логарифм гамма-функции 
		elif num == 'lgamma':
			a = float(input("A: "))
			print(math.lgamma(a))
		# Площадь треугольника
		elif num == 'Striangle':
			a = float(input('A: '))
			b = float(input('B: '))
			c = float(input('C: '))
			print((a + b + c) / 2)
		# Площадь круга
		elif num == 'Scircle':
			R = float(input('Радиус: '))
			print(math.pi * R)
		# Площадь квадрата
		elif num == 'Ssquad':
			a = float(input('A: '))
			print(a * a)
		# Площадь прямоугольника
		elif num == 'S':
			a = float(input('A: '))
			b = float(input('B: '))
			print(a * b)
		# Периметр круга
		elif num == 'Pcircle':
			R = float(input('Радиус: '))
			print(6.28318530718 * R)
		# Периметр квадрата
		elif num == 'Psquad':
			a = float(input('A: '))
			print(a * 4)
		# Периметр прямоугольника
		elif num == 'P':
			a = float(input('A: '))
			b = float(input('B: '))
			print((a + b) * 2)
		# Периметр треугольника
		elif num == 'Ptriangle'
			a = float(input('A: '))
			b = float(input('B: '))
			c = float(input('C: '))
			print(a + b + c)
 	# Произойдет если в num не будет значения операции 
	else:
		print("Неправильное значение!")
