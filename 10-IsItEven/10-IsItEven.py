def numbcheckerIO(userinput):
    userinput1 = int(userinput)
    return userinput1
    
def numberchecker(userinput):
    userinput2 = userinput % 2
    
    if userinput2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.") 

while True:
 number = numbcheckerIO(input("Enter number here: "))
 numberchecker(numbcheckerIO(number))
