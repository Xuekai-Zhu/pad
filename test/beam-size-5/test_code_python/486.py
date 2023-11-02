def solution():
    
    # Define the cost of the toy car and the initial savings
    CAR_COST = 12
    INITIAL_SAVINGS = 4

    # Define the amount of money saved per day
    SAVINGS_PER_DAY = 2

    # Calculate the remaining amount of money
    remaining_money = CAR_COST - INITIAL_SAVINGS

    # Calculate the number of days it will take to save the remaining amount
    days_to_save = remaining_money / SAVINGS_PER_DAY

    # Display the number of days it will take to save the remaining amount
    result = days_to_save
    return result

print(solution())