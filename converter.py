# Create an interface where the user enters information

print("Welcome")
print("...")
converter = input("What would you like to convert? ('Fahrenheit' or 'Celsius'): ")

#Make it into a function 
def ying_yang():
    if converter.lower() == 'fahrenheit':
        Fahrenheit = float(input("What is the Fahrenheit?: "))
        Celsius = (Fahrenheit - 32) * 5 / 9 
        print(f"{Fahrenheit} Fahrenheit is equal to: {Celsius} Celsius")
    elif converter.lower() == 'celsius':
        Celsius = float(input("What is the Celsius?: "))
        Fahrenheit = Celsius * 9 / 5 + 32
        print(f"{Celsius} Celsius would be equal to:{Fahrenheit} Fahrenheit ")

    else:
        print("Better Luck Next Time: ")

#Output

ying_yang()

