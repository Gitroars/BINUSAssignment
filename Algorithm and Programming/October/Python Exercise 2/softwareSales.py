retailPrice = 99
numberOfPackagesPurchased = int(input("Enter the number of packages purchased : "))

Price = (retailPrice*numberOfPackagesPurchased)

if(19>=numberOfPackagesPurchased>=10):
    discountAmount = 10
elif (49>=numberOfPackagesPurchased>=20):
    discountAmount = 20
elif (99>=numberOfPackagesPurchased>=50):
    discountAmount = 30
elif (numberOfPackagesPurchased>=100):
    discountAmount = 40
else:
    discountAmount = 0

discount = (discountAmount/100)*Price
totalPrice = Price - discount

print(f"Discount Amount @ {discountAmount}% : ${discount}"  )
print(f"Total Amount : ${totalPrice} ")
