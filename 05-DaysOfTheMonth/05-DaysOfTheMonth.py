dict = { 
        "1": "31",
        "2": "28",
        "3": "31",
        "4": "30",
        "5": "31",
        "6": "30",
        "7": "31",
        "8": "30",
        "9": "31",
        "10": "30",
        "11": "31",
        "12": "30"} # definin the dictionary.

user_input = (input("Enter the month number: ")) # asks the user to input the number of the month they wish to enquire about.

if user_input in dict: # checks the validity of the user's input.
     print("There are " + dict[user_input] + " days in the month.")
else: 
     print("Invalid input.")

while user_input == "2": # this block of code fires when the user inputs "2."
 if user_input == "2":
     leapyearquery = input("Is the current year a leap year? (y/n) ").lower() # asks the user if it is presently a leap year.
 
 if leapyearquery == "y":
      print("February has 29 days this year because it's a leap year.")
      break
 
 elif leapyearquery == 'n':
      print("February has 28 days this year because it's not a leap year.")
      break
 else: # fires when the user doesn't enter a valid answer.
       print("Invalid input. Please respond only with either 'y' or 'n'") # prints when the user enters anythin other than "y" and "n" in response to the query.