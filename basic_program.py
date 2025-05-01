
#print("Hello world")


#converting celsius to fahrenheit

c = input("Enter celsius: ")
c = float(c)
f = (c * 9/5) + 32
print("Farenheit: ",f)


#converting fahrenheit to celsius
f = input("Enter farenheit: ")
f = float(f)
c = (f -32) * 5/9
print("Celsius: ",c)


#SI calculator
p = float(input("Enter the principal amount: "))
t = float(input("Enter the time: "))
r = float(input("Enter the rate of interest: "))
simple_interest = (p * t * r)/100
print("simple interest is: ",simple_interest)