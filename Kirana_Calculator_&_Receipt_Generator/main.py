from datetime import datetime # To get current time and date
import random
import string

sum = c = 0 #Intialising variables
d = string.digits
print("SMART STORES")
receipt_no = random.choice(d) # Generating a unique receipt number for each bill
lItem = [] #Empty list
qty = []
pItem = []

while True:
    item = input("Enter item name: ")
    if(item != 'q'):
        lItem.append(item)
        c+= 1
        qt = float(input("Enter Quantity(in kgs/ gs/ pkts/ piece): "))
        qty.append(qt)
        price_of_item = float(input("Enter price of items:\n"))
        pItem.append(price_of_item)

        if(qt >= 1): # Diff. in kgs. & gms.
            sum+= (price_of_item*qt)
        else:
            sum+= (price_of_item*qt)

        print(f"Your current bill is {sum}.\n Total no. of items you purchased is {c}. Want to add more items or Press 'q' to exit. ")
    else:  
        # Prints a digital receipt for each purchase
        print("\n")
        print(f"Receipt Bill\nReceipt.No: {receipt_no}")
        now = datetime.now()
        print(now) #Prints current date and time
        print("Item\t Qty\t Price \n")
        for i in range(len(lItem)):
            if(qty[i] >= 1):
                print(f"{lItem[i]}\t {qty[i]}\t {pItem[i]}\n")
            else:
                print(f"{lItem[i]}\t {qty[i]*1000}gms\t {pItem[i]}\n") 

        print(f"Subtotal: Rs.{round(sum)} \n Thank you for visiting us.") 
        break






