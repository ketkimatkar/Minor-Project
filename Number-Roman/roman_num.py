def printNum(roman):
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    list1=list(roman)                                   #to split roman into list for eg.["C","C","C"]
    sum=0
    for ch in list1:
        if ch in sym:
            i=sym.index(ch)                            #if ch is found index of ch in list is stored in i
            sum=sum+num[i]                             #corresponding number of roman will be added to sum
    return sum
roman=input("Enter roman numeral of your choice:")
print("Converted version of roman is :",printNum(roman))
