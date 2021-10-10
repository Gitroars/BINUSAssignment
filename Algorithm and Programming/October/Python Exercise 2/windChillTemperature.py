temperature = eval(input("Enter the temperature in Fahrenheit: "))

while not(41>temperature>-58):
    print("Temperature must be between -58F and 41F")
    temperature = eval(input("Please re-enter the temperature in Fahrenheit: "))

windSpeed = eval(input("Enter the wind speed miles per hour : "))

while not(windSpeed>=2):
    print("Speed must be greater than or equal to 2")
    temperature = eval(input("Please re-enter the temperature in Fahrenheit: "))

Twc = 35.74 + (0.6215*temperature) - (35.75*(windSpeed**0.16)) + (0.4275*(temperature**0.16))
print(f"The wind chill index is {(round(Twc,3))}")