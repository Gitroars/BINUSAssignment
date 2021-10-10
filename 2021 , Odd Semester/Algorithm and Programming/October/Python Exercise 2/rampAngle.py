import math

mass = eval(input("Enter the mass of the cart (in kg): "))
force = eval(input("Enter the force to push the cart (in N):  "))
g = 9.8

sinX = force/(mass*g)
x = math.asin(sinX)
x = math.degrees(x)
print(f"The angle of the ramp is {round(x,1)}")