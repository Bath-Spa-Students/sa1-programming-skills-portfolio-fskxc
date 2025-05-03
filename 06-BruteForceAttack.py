#create a variable for the correct password
correct_password = "12345"

while True:
    entry = input("Enter the password: ")
    
    if entry == correct_password:
        print("Access granted!")  
        break  #this stops the loop when the right password is entered
    else:
        print("Wrong password, try again.") 