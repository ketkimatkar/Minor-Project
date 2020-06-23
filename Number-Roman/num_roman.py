def printRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    i=12
    roman=""
    while number>0:
        quo=number//num[i]                 #to obtain quotient when number is divided by num[i]
        number=number%num[i]               #when number is divided by num[i],remainder will be the next number
        while quo>0:
            roman=roman+sym[i]             #to concantenate roman numerals
            quo=quo-1
        i=i-1
    return roman
num=int(input("Enter the number:"))
print("Roman of entered number is:",printRoman(num))

