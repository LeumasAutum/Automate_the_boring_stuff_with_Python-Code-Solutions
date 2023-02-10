# Input Validation
# Add try and except statements to the previous project to detect whether the 
# user types in a noninteger string. Normally, the int() function will raise a 
# ValueError error if it is passed a noninteger string, as in int('puppy'). In the 
# except clause, print a message to the user saying they must enter an 

def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result

while True:
    try:
        number = int(input("Enter number: "))
        break
    except ValueError:
        print("You must enter an integer.")

while number != 1:
    number = collatz(number)