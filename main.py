import math
print(math.sin(45))
print(math.cos(45))
print(math.tan(45))

print(math.ceil(45.490))
print(math.floor(45.890))
print(math.factorial(5))

x = 10
y = -15
#using copysign function
print('the value of x after copyingthe sign from y is: ' +str(math.copysign(x, y)))

#using fabs and gcd function
print('Absolute value of -96 and 56 are: ' + str(math.fabs(-90)) + ', ' + str(math.fabs(56)))

print('The GCD of 24 and 56 : ' + str(math.gcd(24, 56)))