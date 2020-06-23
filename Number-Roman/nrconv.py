choice=int(input("Enter you choice for conversion:\n 1-Number to Roman \n 2-Roman to Number"))
if choice==1:
    import num_roman                #num_roman.py will be executed
elif choice==2:
    import roman_num                #roman_num.py will be executed
else:
    print("You have entered wrong choice")
