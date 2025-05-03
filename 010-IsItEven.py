def check_even_odd(number):
    if number % 2 == 0:  #a modulo operator, number divided by 2 leaves a remainder of zero
        return "That number is even"  
    else:
        return "That number is odd"   

def main():
    # ask user for a number and convert to int
    user_input = int(input("Enter a number: "))
    
    # call the check function and get the message
    result = check_even_odd(user_input)
    
    # Print the result
    print(result)

if __name__ == "__main__":
    main()