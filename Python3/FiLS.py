#FiLS - FIbonacci, Laws and Sunflowers

author = 'Roberto Bastone'
email = 'robertobastone93@gmail.com'

version = 1.03
sunflower_colour = '#fe7d00'

################################################### IMPORT
from mpmath import mp
mp.dps = 30
from termcolor import colored
import numpy as np
import matplotlib.pyplot as plt

################################################### CLASS
class FiLS:
	yes = {'Y','y','YES','yes','Yes'}
	no = {'N','n','NO','no','No'}

	def __init__(self):
		self.i = 1
		self.num = 1
		self.SUM = 0
		self.a = 1.
		self.b = 1.
		ratio = []
		print( colored("Initializing... FIbonacci, Law and Sunflowers (FiLS) version " + str(version), 'blue') )
		print( colored("(Author: " + author+')', 'blue') )
		print( colored("For info - or anything else - please, feel free to reach me at " + email, 'blue') )

	def main(self):
		self.FiLS_introduction(self.yes,self.no)
		self.choosingSubroutine()

	def FiLS_introduction(self,yes,no):
		while True:
			choice = input(">FiLS has several subroutines at the moment. Do you want me to explain what each of them does? [y/n] \n").lower()
			if choice in yes:
				print(">1) By typing \"fib\", FiLS will show you the first n terms of the Fibonacci sequence. ")
				print(">2) By choosing \"sum\", FiLS will calculate the sum of the first n terms of the sequence. ")
				print(">3) By selecting \"gold\", FiLS will output the ratios of the adjacent terms for the first n terms of the sequence and, as well, produce a plot showing how it varies. ")
				print(">4) By typing \"sunflower\", FiLS will reproduce the sunflower seed pattern that presents spirals following the Fibonacci sequence. \n")
				break
			elif choice in no:
				print(">Okay, let us continue.")
				break
			else:
				print(">Please, select [y/n] only")
				continue

	def choosingSubroutine(self):
		while True:
			fnct = input(">What function do you choose? ").lower()
			if ( fnct == "fib"):			#fib function
				integer = int(input(">Choose the number of integers you want to show: "))
				print(int(self.num))
				while ( self.i <= integer-1):
					print(int(self.num))
					self.num = self.a + self.b
					self.a = self.num
					self.b = self.num - self.b
					self.i = self.i +1
				break
			elif ( fnct == "sum"):			#sum function
				integer = int(input(">Choose the number of integers you want to sum: "))
				while (self.i<= integer):
					SUM = SUM + self.num
					self.num = self.a + self.b
					self.a = self.num
					self.b = self.num - self.b
					self.i = self.i + 1
				print(int(SUM))
				break
			elif ( fnct == "gold"):
				integer = int(input(">Choose the number of terms of the sequence: "))
				while ( self.i <= integer):
					print(str.format('{0:.30f}', self.a/self.b))
					self.num = self.a + self.b
					self.a = self.num
					self.b = self.num - self.b
					self.i = self.i +1
					self.ratio.append(self.a/self.b)
				print(">Fibonacci sequence tends towards the golden ratio which is")
				print(mp.phi)
				j = np.linspace(1,integer,integer)
				plt.figure( figsize=(7,5))
				plt.axhline(mp.phi, label='golden ratio', color='red')
				plt.scatter(j,self.ratio, label='ratio')
				plt.plot(j,self.ratio)
				plt.ylabel("Ratio of adjacent terms")
				plt.xlabel("Sequence terms")
				plt.ylim(1,2)
				plt.xlim(1,integer)
				plt.legend()
				plt.show()
				break
			elif ( fnct == "sunflower"):
				integer = int(input(">Choose the number of terms for the seed pattern (for a better result choose at least 1000): "))
				golden_angle = 2.39996322972865332   #radians
				sunflower_colour = '#fe7d00'
				frame = 7                            # size of plot
				disc_florets = np.array(np.linspace(0,integer,integer+1))
				angular_separation = disc_florets * golden_angle
				def sunflower(dist,angle):
					x = dist * np.cos(angle)
					y = dist * np.sin(angle)
					plt.figure(figsize=(frame,frame))
					plt.scatter(x,y,color=sunflower_colour)
					plt.axis('off')
					plt.tight_layout()
					plt.show()
				sunflower(np.sqrt(disc_florets),angular_separation)               #sqrt for better visualization
				break
			else:
				print(">Error! Type a valide entry")
				continue
