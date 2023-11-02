def solution():
    """Shelly has ten $10 bills and four fewer $5 bills. How much money does Shelly have in all?"""
    
    # Define the value of each bill
    TEN_VALUE = 10
    FIVE_VALUE = 5
    
    # Define the number of $10 bills Shelly has
    ten_bills = 10
    
    # Calculate the number of $5 bills Shelly has
    five_bills = ten_bills - 4
    
    # Calculate the total value of Shelly's money
    total_value = ten_bills * TEN_VALUE + five_bills * FIVE_VALUE
    
    # Display the total value of Shelly's money
    result = total_value
    return result

print(solution())