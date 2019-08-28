'''
myloanwhat.py
This Calculator Takes the Standard Amortization Calculator
And uses it to calculate how much your loan is effectively for when
You account for the interest you pay over the life of the loan.

Amortization formula is
A = P * ((r**n)*(r-1))/((r**n) - 1)
where A = payment amount per period (monthly payment)
P = initial principle
r = interest rate (per period). So if annual interest is 4%,
you would divide that by 12
n = total number of payments
'''

import math
print("Hello, this is MY LOAN WHAT, where we tell you how much you really signed up for!")
print("What was your original loan amount?  $")
amount = input()
iP = float(amount) #Input the initial principle balance of the loan.
cP = iP
print("How many years is your loan spread out for?")
print("Years: ")
years = input()
n = float(30*12) #Number of months
print("What is your interest rate? %")
rate = input()
r = float(rate) #Interest rate
r = r/12/100 #convert to decimal for calculation, and divide by 12 mo
A = iP*(r*((1+r)**n))/(((1+r)**n)-1) #calculate monthly payment amount
interest = 0 #initialize interest value

while (n > 0):
	i = cP*r #calculate this month's interest
	p = A - i #calculate principle to be applied
	interest = interest + i #add interest to total
	cP = cP - p
	n = n-1
	if (cP<=.01):
		loan = interest+iP 
		print("Your loan is actually $"+str(loan)+".")
		print("You are paying an extra $"+str(interest)+" in interest.")
		break