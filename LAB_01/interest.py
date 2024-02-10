princ = int(input("Enter a principal"))
time = int(input("Enter time in months"))
rate = int(input("Enter rate of interest"))

simpint = (princ * rate * time)/100

print("SI = ", simpint)
print("Amount = ", simpint + princ)