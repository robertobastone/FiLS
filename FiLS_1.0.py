#Fibonacci sequence

# author: Roberto Bastone

version = 1.0
methods = "two"

# code

print "Welcome to the Fibonacci List and Sum (FiLS) version ", version 
print "You can choose", methods," different functions: type \"fib\" to show the first n terms of the sequence or \"sum\" to get the sum of the first n terms. \n"

i = 1 #index
num = 1	#initializing variables
SUM = 0
a = 1
b = 1

while True:
	fnct = raw_input("What function do you choose? ").lower()
	if ( fnct == "fib"):			#fib function
		int = int(raw_input("Choose the number of integers you want to show: "))
		while ( i <= int):
			print(num)
			num = a + b
			a = num
			b = num - b
			i = i +1
		break
	elif ( fnct == "sum"):			#sum function
		int = int(raw_input("Choose the number of integers you want to sum: \t"))
		while (i<= int):
			SUM = SUM + num
			num = a + b
			a = num
			b = num - b
			i = i + 1
		print(SUM)
		break
	else:
		print("Error! Type \"fib\" or \"sum\" ")
		continue
