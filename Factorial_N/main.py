# Part 1 : Calculate the factorial of a given number
# Part 2 : Find the number of trailing zeros in that factorial
def fact(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return num*fact(num-1)
    
def factTrailZeros(num): # Camel Casing
    count = 0
    i = 5
    while(num/i != 0): # Most logical approach
        count += int(num/i)
        i = i*5
    return count

if __name__=='__main__':
    num = int(input("Enter a number. \n"))
    choice = int(input("Enter Your Choice:\n1. Factorial of a Number\n2. Trailing Zeros of a Factorial\n3. Both (1) or (2)\n"))
    
    match choice:
        case 1:
            print(f"Factorial of {num} is {fact(num)}")  
        case 2:
            print(f"Trailing number of zeros of factorial of {num} is {factTrailZeros(num)}")  
        case 3: # Default Case in Pyhton
            print(f"Factorial of {num} is {fact(num)}")  
            print(f"Trailing number of zeros of factorial of {num} is {factTrailZeros(num)}")  
        case _:
            print("Invalid Choice. RE-ENTER!")
                





        
        