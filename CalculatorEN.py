#modules import
#mathematics for math.sqrt, sin, cos, tan, hypot.
import math
#time for exit
import time
#while
while True:
	#first line guess will be print
	num = input("Write any sign of the calculation if the value is equal to zero, the process ends(+, -, /, *, //, **, sqrt, sin, cos, tan, hypot): ")
	#exit
	if num == ("0"):
		print ("The procces will ends in 3 seconds")
		time.sleep(3)
		break
	#check an ops
	if num in ("+, -, /, *, //, **, sqrt, sin, cos, tan, hypot"):
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
	#if in num haven't current value 
	else:
		print("Bad value!")
