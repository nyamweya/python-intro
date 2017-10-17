#mathliblary
'''import math
x=input('Enter your radius: ')
area=math.pi * math.pow(x,2)
perimeter=math.pi * (x+x)
print "The area of a circle with that radius is %s \nThe perimeter is %s" %(area,perimeter)'''

#user inputs
'''name=raw_input("Whats's your name?: ")
if len(name)> 5:
	print "You are Tall"
elif len(name)==5:
	print "You are perfect"
else:
	print "You are Short"
num=input("Enter your number: ")
if (num % 2 ==0):
	print "Even"
else:
print "Odd"'''

#get max and min
'''x=input("Enter your first number: ")
y=input("Enter your second number: ")
print max(x,y)'''

#range
'''x=range(1,51)
for i in x:
	if i%2==0:
		print "Even "+str(i)
	else:
		print "Odd "+str(i)'''
#print no. bigger than 20
'''import math
a=[24,17,15,30,1,8,19,45]
for i in a:
	if i>20:
		print i'''

#Dictionaries
'''Ccodes={'kenya':22,'Ug':256,'Tz':0}
print Ccodes
Ccodes['Rwanda']=250
Ccodes['kenya']=254
Ccodes['Tz']=255
print Ccodes'''

#function
'''import math
x=input('Enter your radius: ')
area=math.pi * math.pow(x,2)
perimeter=math.pi * (x+x)
print "The area of a circle with that radius is %s \nThe perimeter is %s" %(area,perimeter)'''

'''import math
def r():
	radius=input("Enter radius: ")
	return radius
radius1=r()

def area(r):
	area=math.pi * math.pow(r,2)
	return area
def per(r):
	per=math.pi * (r+r)
	return per
print "The area of the circle is",area(radius1)
print "The perimeter of the circle is:",per(radius1)'''



#palyndron
def pal():
	word=raw_input("Enter word: ")
	return word
word1=pal()

if pal==polyndron:
	print True
else:
	print False
