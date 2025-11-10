Name = input("Name: ")
Age = input("Age: ")
Hometown = input("Hometown: ") # Declaring variables and tying them to inputs. 

print("________") # I just thought it'd make the output look cleaner in the console.
print("Biographical Information:")
print(f"""Name: {str(Name)}
Age: {str(Age)}
Hometown: {str(Hometown)}""") # I converted all of the user's inputs into strings before printing in order to avoid issues.