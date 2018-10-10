#modules import
#mathematics for math.sqrt, sin, cos, tan, hypot more
import math
#time for exit
import time
#while
while True:
	#first line guess will be print
	print("Write any sign of the calculation if the value is equal to zero, the process ends(+, -, /, *, //, **, sqrt, sin, cos, tan, hypot, ")
	num = input("log, log1p, log10, log2, degress, radians, asin, acon, atan, atan2, sinh, cosh, tanh, asinh, acosh, atanh, gamma, lgamma, Scircle, Ssquad, S, Pcircle, P, Psquad")
	#exit
	if num == ("0"):
		print ("The procces will ends in 3 seconds")
		time.sleep(3)
		break
	#check an ops
	if num in ("+, -, /, *, //, **, sqrt, sin, cos, tan, hypot, log, log1p, log10, log2, degress, radians, asin, acon, atan, atan2, sinh, cosh, tanh, asinh, acosh, atanh, gamma, lgamma, Scircle, Ssquad, S, Pcircle, P, Psquad"):
		#first op(+)
		if num == '+':
			x = float(input("First number= "))
			y = float(input("Second number= "))
			print((x+y))
		#second op(-)
		elif num == '-':
			x = float(input("Fisrt number= "))
			y = float(input("Second number= "))
			print((x-y))
		#third op(*)
		elif num == '*':
			x = float(input("Fisrt number= "))
			y = float(input("Second number= "))
			print((x*y))
		#fourth
		elif num == '/':
			x = float(input("Fisrt number= "))
			y = float(input("Second number= "))
			#check on errors
			try:
				print((x/y))
			except ZeroDivisionError:
				#print if error detected
				print("ZeroDivision!")
		#how many second numbers in first number 
		elif num == '//':
			x = float(input("First number= "))
			y = float(input("Second number= "))
			try:
				print((x//y))
				print((x%y))
			except ZeroDivisionError:
				print("ZeroDivision!")
		#grade
		elif num == '**':
			x = float(input("First number= "))
			y = float(input("Second number= "))
			print((x**y))
		#sqrt(what number need will be multiply by itself to take this number)
		elif num == 'sqrt':
			try:
				x = float(input("Number for sqrt operation: "))
				y = 0
				print((math.sqrt(x)))
			except ZeroDivisionError:
				print("ZeroDivision!")
		#sinus
		elif num == 'sin':
			try:
				x = float(input("A: "))
				print((math.sin(x)))
			except ValueError:
				print("Don't try lie to me, I'm cool AI!")
		#cosinus
		elif num == 'cos':
			#try to fix error if user will be write a string 
			try:
				x = float(input("A: "))
				print((math.cos(x)))
			except ValueError:
				print("Don't try lie to me, I'm cool AI!")
		#tangens
		elif num == 'tan':
			try:
				x = float(input("A: "))			
				print((math.tan(x)))
			except ValueError:
				print("Don't try lie to me, I'm cool AI!")
		#hypotenuse
		elif num == 'hypot':
			try:
				x = float(input("A: "))
				y = float(input("B: "))
				print((math.hypot(x, y)))
			except ValueError:
				print("Don't try lie to me, I'm cool AI!")
		# Logarithm
		elif num == 'log':
			a = float(input("Number: "))
			print(math.log(a))
		# Natural logarithm
		elif num == 'log1p':
			a = float(input("Number: "))
			print(math.log1p(a))
		# Log A on base 10
		elif num == 'log10':
			a = float(input("Number: "))
			print(math.log10(a))
		# Логарифм A по основанию 2
		elif num == 'log2':
			a = float(input("Number: "))
			print(math.log2(a))
		# Converts radians to degrees
		elif num == 'degress':
			a = float(input("Radians: "))
			print(math.degrees(a))
		# Converts degrees to radians.
		elif num == 'radians':
			a = float(input("Degress: "))
			print(math.radians(a))
		# Arcsine in radians
		elif num == 'asin':
			a = float(input("A: "))
			print(math.asin(a))
		# Arccosine radians
		elif num == 'acos':
			a = float(input("A: "))
			print(math.acos(a))
		# Arctangent in radians
		elif num == 'atan':
			a = float(input("A: "))
			print(math.atan(a))
		# Arctangent in radians, taking into account the quarter in which the point is located
		elif num == 'atan2':
			a = float(input("A: "))
			b = float(input("B: "))
			print(math.atan2(a, b))
		# Brings out the hyperbolic sine
		elif num == 'sinh':
			a = float(input("A: "))
			print(math.sinh(a))
		# Brings out hyperbolic cosine
		elif num == 'cosh':
			a = float(input("A: "))
			print(math.cosh(a))
		# Brings out hyperbolic tangent
		elif num == 'tanh':
			a = float(input("A: "))
			print(math.tanh(a))
		# Combs back hyperbolic sine
		elif num == 'asinh':
			a = float(input("A: "))
			print(math.asinh(a))
		# Brings back hyperbolic cosine
		elif num == 'acosh':
			a = float(input("A: "))
			print(math.acosh(a))
		# Brings back hyperbolic tangent
		elif num == 'atanh':
			a = float(input("A: "))
			print(math.atanh(a))
		# Gamma func
		elif num == 'gamma':
			a = float(input("A: "))
			print(math.gamma(a))
		# Natural logarithm of gamma func
		elif num == 'lgamma':
			a = float(input("A: "))
			print(math.lgamma(a))
		# Circle area
		elif num == 'Scircle':
			R = float(input('Degress: '))
			print(math.pi - R)
		# Square area
		elif num == 'Ssquare':
			a = float(input('A: '))
			print(a * a)
		# Rectangle area
		elif num == 'S':
			a = float(input('A: '))
			b = float(input('B: '))
			print(a * b)
		# Perimeter of circle
		elif num == 'Pcircle':
			R = float(input('Radius: '))
			print(6.28318530718 * R)
		# Perimeter of square
		elif num == 'Psquare':
			a = float(input('A: '))
			print(a * 4)
		# Perimeter of rectangle
		elif num == 'P':
			a = float(input('A: '))
			b = float(input('B: '))
			print((a + b) * 2)
	#if in num haven't current value 
	else:
		print("Bad value!")
