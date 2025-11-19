name = input("Name: ")
age = input("Age: ")
hometown = input("Hometown: ") # Declaring variables and tying them to inputs. 

bio_info = { 
                       "name": name,
                       "age": age,
                       "hometown": hometown
 } 

print("________") # I just thought it'd make the output look cleaner in the console.
print("Biographical Information:")

print("Name: " + bio_info["name"])
print("Age: " + bio_info["age"])
print("Hometown: " + bio_info["hometown"])