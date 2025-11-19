while True: # added this here to restart the code in case the user made an error.
 names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] # initialisin the list
 userinput  = input("Search for a name here: ") # asks for the user's input

 if userinput in names: # checks if the name that the user put in is in the list.
    print(userinput + " is in the list.")
    break 
 else: 
    print("That name is not in the list.")
    continue