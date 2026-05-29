from cleanup import clear_screen, returnn
from add import addition
from sub import subtraction
from mult import multiplication
from div import division

def main():
    while True:
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Clear")
        print("6. Exit")

        option = input("\nChoose an option: ")

        if option == '6':
            clear_screen()
            break
        elif option == '5':
            clear_screen()
            continue

        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))


        if option == '1':
            result = addition(num1, num2)
            print(f"Result: {result}")
        elif option == '2':
            result = subtraction(num1, num2)
            print(f"Result: {result}")
        elif option == '3':
            result = multiplication(num1, num2)
            print(f"Result: {result}")
        elif option == '4':
            result = division(num1, num2)
            print(f"Result: {result}")
        else:
            print("Invalid.")
        
        returnn()
        clear_screen()
   

if __name__ == '__main__':
    main()