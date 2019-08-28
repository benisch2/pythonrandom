'''
Life Waster

It's amazing how often we waste time.
But exactly how much time per year are you wasting?
Now you can find out!
'''
import math
import roundt

print("We all waste time, but exactly how much are you wasting?")
print("Wouldn't you like to know?")
print("Enter an activity that you do that you feel is a waste of time:")
waste = str(input())
print("How many time do you waste doing this?")
print("Please tell us how many minutes you waste each time you do this:")
print("(If multiple hours, type H)")
Min0 = input()
'''
if Min0 == "H" or "h":
	print("Please tell us how many hours you waste each time you do this:")
	Min0 = input()
	Min0 = int(Min0)
	Min0 = Min0*60
'''
Min0 = int(Min0)
print("How many days a week do you do this? If you do this less than once a week, enter 0.")
wk = input()
wk = int(wk)
if wk > 0:
	twaste = Min0*wk*52
if wk == 0:
	print("How many times a month do you do this? If you do this less than once a month, enter 0.")
	mnth == input()
	if mnth > 0:
		twaste = Min0*mnth*12
	if mnth == 0:
		print("How many times a year do you do this?")
		yr = input()
		if yr > 0:
			twaste = Min0*yr
		if yr == 0:
			print("Well I guess you don't waste any time, then. Showoff.")
fwaste = float(twaste)
hwaste = roundt.roundit((fwaste/60),2) 
dwaste = roundt.roundit((fwaste/60/24),2) 
wwaste = roundt.roundit((fwaste/60/24/7),2) 


print("Congratulations, slacker! You waste " + str(twaste) + " minutes " + waste + " every year!")
if twaste >= 60:
	print("That's a total of:")
	print(str(hwaste) + " hours!")
	if hwaste >= 24:
		print("Or " + str(dwaste) + " days!")
		if dwaste >= 7:
			print("Or " + str(wwaste) + " weeks!")
print("I hope you're proud of yourself! Ya filthy animal!!!")