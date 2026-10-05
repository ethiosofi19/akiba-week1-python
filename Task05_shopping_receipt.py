# Ethiopian Shopping Receipt

customer_name = input("What's your name dear customer? ")
product_name = input("What product do you want? ")
price = input("What is its price? ")
quantity = input("How many of these products do you want? ")

total = int(quantity)*int(price)

print("======================================== \n       RECEIPT \n========================================")
print("\nCustomer: " + customer_name,"\n")
print("Product \t Price \t\t Qty")
print("----------------------------------------")
print(product_name ,"\t", price+"ETB","\t" , quantity,"\n")
print("Total: \t", str(total),"\n")

print("Thank you for shopping!")
print("========================================")



