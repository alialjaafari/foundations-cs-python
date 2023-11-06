
items=[["tomato",1],["potato",2],["chocolate",3],["tea",4],["coffee",5]]
coupon= 0

def addItem():
    item = input("Enter the name of the item: ")
    price = float(input("Enter the price of the item: "))
    quantity = int(input("Enter the quantity: "))
    
    if item in items:
        newOrder[item]['quantity'] += quantity
        
def checkTotal():
        total = sum(item['price'] * item['quantity'] for item in items())
        print("The total of your bill is: ", total)
       
def addCoupon():
    coupon= 0 
    coupon_value = float(input("Enter the coupon value: "))
    coupon += coupon_value
        
def checkout():
        print("Items bought and their quantities:")
        for item in items():
            print("item: item['quantity'] x item['price']")

        total_order = sum(item['price'] * item['quantity'] for item in items())
        print("Total of the order (without coupons): ", total_order)

        print("Total of the coupons: ", coupon)

        total_to_pay = total_order - coupon
        print("Total to pay: ", total_to_pay)

def newOrder():
  choice=-99
  while choice !=4:
    print("Enter")
    print("1. to add an item")
    print("2. to check total")
    print("3. to add a coupon")
    print("4. to checkout")

    choice=int(input())

    if choice==1:
      addItem()
    elif choice ==2:
      checkTotal()
    elif choice ==3:
      addCoupon()
    elif choice ==4:
      checkout()
    else:
      print("ivalid input")
  

def mainMenu():
  choice=-99 
  while choice !=2:
    print("Enter")
    print("1. to start a new order")
    print("2. to close the program")
    
    choice=int(input())
    
    if choice==1:
      print("starting a new order...")
      newOrder()
    elif choice ==2:
      print("bye bye")
    else:
      print("ivalid input")


mainMenu()

