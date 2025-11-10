maximum_attempts = 5 # I started by declaring the variables that are needed to help track the user's attempts.
number_of_attempts = 0

password = "Apple" # I declare the password.

while number_of_attempts < maximum_attempts: # This loops the code until either the user enters the correct password or they exceed the maximum allowed number of attempts.
 print("Passwords are case-sensitive.")
 attempt = input("Please input password: ") 
   
 if attempt == password:
     print("Log-in confirmed.")
     break # This terminates the while loop if the input password is correct.
 else:
     number_of_attempts += 1 # This adds 1 to the mentioned variable whenever an iteration is run (in this case, every retry of password entry.)
     print("Incorrect password.")
     print(f"You have {(maximum_attempts) - (number_of_attempts)} attempts left.") # 5 minus the current number of attempts a user has made at password input.
     
else: # Happens when the user eats up all of their alloted attempts at input.
   print("Incorrect password entered too many times.")
   print("Administrator has been notified.") 
             
      

   
 
 
 
 
 
    

    