# Counting the number of digits
def count_Digits(num):
    c = 0
    temp = num
    while(temp > 0):
        c+= 1
        temp//= 10
    return c

# Calculating sum of digits
def isArmstrong(num):
    s = 0
    temp = num
    while(temp > 0):
        s+= ((temp%10)**count_Digits(num))
        temp//= 10
    return s

# Finding Armstrong number in a given range
def range_Armstrong(start, end):
    s = 0
    print("Armstrong Numbers in range {start} to {end}:\n")
    for i in range(start, end):
        temp = i
        while(temp > 0):
            s+= ((temp%10)**len(str(i)))
            temp//= 10
        if(s == i):
            print(s)
        temp = 0
        s = 0
        
if __name__=='__main__':
    choice = int(input("Enter Your Choice:\n1. Checking a number is Armstrong or not\n2. Finding Armstrong number in a given range\n"))
    #User-driven Menu
    match choice:
        case 1: 
            # Checking Armstrong Number
            num = int(input("Enter a number. \n"))
            if(isArmstrong(num) == num): 
                print(f"Armstrong Number of Order {count_Digits(num)}")
            else:
                print("Not a Armstrong Number")
        case 2:
            # Finding Armstrong number in a given range
            start = int(input("Enter starting point. \n"))
            end = int(input("Enter end point. \n"))
            range_Armstrong(start,end)
        case _:
            print("Invalid Choice. RE-ENTER!")
