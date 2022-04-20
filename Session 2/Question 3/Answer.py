products = ["toothpaste", "shampoo", "shower gel", "soap", "deodorant", "toilet paper", "bleach", "cleaning cloth", "sponge", "detergent", "trash bag", "dog food", "cat food", "cat litter", "dog treat", "cat treat"]
stocks = [32, 41, 18, 27, 6, 23, 20, 38, 34, 40, 22, 40, 38, 40, 34, 3]
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
# we can store at most 50 of each item

finished = False
    
while not finished:
    operation = input() # 'return' or 'buying' or 'exit'
    while operation not in ['return', 'buying', 'exit']:
        operation = input()
        
    if operation == 'exit':
        finished = True
        break
        
    requested_product = input()
    while requested_product not in products:
        requested_product = input()
    
    requested_amount = int(input())
    while requested_amount <= 0:
        requested_amount = int(input())
        
    i = products.index(requested_product)
    product_stock = stocks[i]

    if product_stock >= requested_amount and operation == "buying":
        old_amount = stocks[i]
        stocks[i] -= requested_amount
        print(old_amount, "=>", stocks[i])
        
    elif operation == "buying" and product_stock == 0:
        print("We don't have this product anymore")
        
    elif operation == "buying" and product_stock < requested_amount:
        old_amount = stocks[i]
        stocks[i] = 0
        print((requested_amount - product_stock), "items could not be bought")
        print(old_amount, "=>", stocks[i])
        
    elif product_stock == 50 and operation == "return":
        print("Stocks are full for", requested_product)
        continue
        
    elif product_stock + requested_amount > 50 and operation == "return":
        old_amount = stocks[i]
        stocks[i] += 50 - product_stock
        print(requested_amount - (50 - product_stock), "items could not be returned")
        print(old_amount, "=>", stocks[i])
        
    elif product_stock + requested_amount <= 50 and operation == "return":
        old_amount = stocks[i]
        stocks[i] += requested_amount
        print(old_amount, "=>", stocks[i])
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE