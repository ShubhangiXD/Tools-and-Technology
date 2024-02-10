def maximum(a, b, c):
    if (a>=b) and (a>=c):
        largest = a
    elif (b>=a) and (b>=c):
        largest = b
    else:
        largest = c
        
    return largest

n1 = int(input('Enter a number: '))
n2 = int(input('Enter a number: '))
n3 = int(input('Enter a number: '))
print("maximum: {0}".format(maximum(n1, n2, n3)))