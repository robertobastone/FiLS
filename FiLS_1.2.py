#Fibonacci sequence

# author: Roberto Bastone
# email: robertobastone93@gmail.com

version = 1.2
methods = "two"

#packages
from mpmath import mp
mp.dps = 30 
import numpy as np
import matplotlib.pyplot as plt

# code

print ">Welcome to the Fibonacci List and Sum (FiLS) version ", version 
yes = {'Y','y'}
no = {'N','n'}

while True:
    choice = raw_input(">FiLS has several subroutines at the moment. Do you want me to explain what each of them does? [y/n] \n").lower()
    if choice in yes:
	print ">1) By typing \"fib\", FiLS will show you the first n terms of the Fibonacci sequence"
        print ">2) By choosing \"sum\", FiLS will calculate the sum of the first n terms of the sequence. "
        print ">3) By selecting \"gold\", FiLS will output the ratios of the adjacent terms for the first n terms of the sequence and, as well, produce a plot showing how it varies. \n"
        break
    elif choice in no:
        print">Okay, let us continue"
        break
    else:
        print(">Please, select [y/n] only")
        continue

i = 1      # index
num = 1	# initializing variables
SUM = 0    # initializing sum
a = 1.      # first term
b = 1.      # second term
ratio = []

while True:
	fnct = raw_input(">What function do you choose? ").lower()
	if ( fnct == "fib"):			#fib function
		integer = int(raw_input(">Choose the number of integers you want to show: "))
		while ( i <= integer):
			print(int(num))
			num = a + b
			a = num
			b = num - b
			i = i +1
		break
	elif ( fnct == "sum"):			#sum function
		integer = int(raw_input(">Choose the number of integers you want to sum: "))
		while (i<= integer):
			SUM = SUM + num
			num = a + b
			a = num
			b = num - b
			i = i + 1
		print(int(SUM))
		break
	elif ( fnct == "gold"):
		integer = int(raw_input(">Choose the number of terms of the sequence: ")) 
                while ( i <= integer):
			print(str.format('{0:.30f}', a/b))  
               		num = a + b
               		a = num
               		b = num - b
               		i = i +1
                        ratio.append(a/b)
           	print ">Fibonacci sequence tends towards the golden ratio which is"
                print mp.phi
                j = np.linspace(1,integer,integer)
            	plt.figure( figsize=(7,5))  
                plt.axhline(mp.phi, label='golden ratio', color='red')
            	plt.scatter(j,ratio, label='ratio')
                plt.plot(j,ratio)
            	plt.ylabel("Ratio of adjacent terms")
            	plt.xlabel("Sequence terms")    
            	plt.ylim(1,2)
                plt.xlim(1,integer)
                plt.legend()
            	plt.show()                
                break
	else:
		print(">Error! Type a valide entry")
		continue
