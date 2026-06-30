import math

def show_menu():
    print("\n --- Advanced Commend-Line Calculator --- ")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Logarithm (log base 10)")
    print("8. Natural Logarithm (ln)")
    print("9. Factorial (x!)")
    print("10. Sine (sin x)")
    print("11. Cosine (cos x)")
    print("12. Tangent (tan x)")
    print("13. Prime Number Check")
    print("14. Exit")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def calculate():
    while True:
        show_menu()
        choice = input("Select an operation (1-14): ").strip()

        if choice == '14':
            print("Exiting calculator. Goodbye!")
            break

        
        if choice in ['1', '2', '3', '4', '5']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == '1':
                print(f"Addition: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"subtraction: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"Multiplycation: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("cannot divide by zero.")
                else:
                    print(f" Division: {num1} / {num2} = {num1 / num2}")
            elif choice == '5':
                print(f"  {num1} ^ {num2} = {math.pow(num1, num2)}")

        elif choice in ['6', '7', '8', '9', '10', '11', '12', '13']:
            num = get_number("Enter number: ")

            if choice == '6':
                if num < 0:
                    print(" Cannot calculate square root of a negative number.")
                else:
                    print(f" Result: √{num} = {math.sqrt(num)}")
            elif choice == '7':
                if num <= 0:
                    print(" Logarithm undefined for values less than or equal to zero.")
                else:
                    print(f" Result: log10({num}) = {math.log10(num)}")
            elif choice == '8':
                if num <= 0:
                    print(" Natural logarithm undefined for values less than or equal to zero.")
                else:
                    print(f" Result: ln({num}) = {math.log(num)}")
            elif choice == '9':
                if num < 0 or not num.is_integer():
                    print(" Factorial is only defined for non-negative integers.")
                else:
                    print(f" Result: {int(num)}! = {math.factorial(int(num))}")
            elif choice == '10':
                # Converts degrees to radians for intuitive user experience
                rad = math.radians(num)
                print(f" Result: sin({num}°) = {round(math.sin(rad),6)}")
            elif choice == '11':
                rad = math.radians(num)
                print(f" Result: cos({num}°) = {round(math.cos(rad),6)}")
            elif choice == '12':
                # Handles undefined tangent values at 90, 270 degrees
                if (num - 90) % 180 == 0:
                    print(f" Result: tan({num}°) is undefined.")
                else:
                    rad = math.radians(num)
                    print(f" Result: tan({num}°) = {round(math.tan(rad),5)}")
            elif choice == '13':
                if not num.is_integer():
                    print(" Prime checking  apply's only to whole integers.")
                else:
                    val = int(num)
                    if is_prime(val):
                        print(f" Result: {val} is a PRIME Number! ")
                    elif val<=1:
                        print(f" Result: {val} is Neither PRIME/COMPOSITE number.")
                    else:
                        print(f"Result: {val} is a COMPOSITE NUMBER")    
        else:
            print(" Invalid selection. Please choose a number from 1 to 14.")

if __name__ == "__main__":
    calculate()
