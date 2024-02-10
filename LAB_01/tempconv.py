def converter(cel):
    faren = ((9/5)*cel) + 32
    return faren

celsius = int(input('Enter a temperature in celsius: '))
print("The temperature {0} is {1} in Farenheit.".format(celsius, converter(celsius)))