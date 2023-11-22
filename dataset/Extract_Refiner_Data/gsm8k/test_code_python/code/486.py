def solution():
    
    # Define the cost of the toy car and the amount already saved
    CAR_COST = 12
    SAVINGS = 4

    # Calculate the remaining amount to be saved
    remaining_amount = CAR_COST - SAVINGS

    # Calculate the number of days it will take to save the remaining amount
    days_to_save = remaining_amount / 2

    # Display the number of days
    result = days_to_save
    return result

print(solution())