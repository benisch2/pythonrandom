'''
Round and Truncate

Ever wanted to round something in python at the end of a calculation
with a nice truncation at the end?
It's dumb that it doesn't come built in, and it's messy dealing
with floats.

This is a function that does just that.

It takes a float, then rounds and truncates as you would expect.

Example inputs and outputs
afloat = 2.54729313022
digits = 2
returns = 2.55

afloat = 2.54729313022
digits = 4
returns = 2.5473
'''

def roundit(afloat, digits): #entered float and the number of digits after decimal you want to truncate 
	a = afloat
	a0 = a%(1.0/(10**digits))
	a = a - a0
	ndigit = int(a0*(10**(digits + 1)))
	if ndigit >= 5:
		a = a + (1.0/(10**digits))
	b = int((a%1)*(10**10)) #basically tests if there's a zero after the first decimal
	if (b == 0):
		a = int(a)
	return a

'''
test = roundit(100.1,4)
print(str(test))
'''

