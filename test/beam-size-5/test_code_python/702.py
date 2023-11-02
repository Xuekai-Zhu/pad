def solution():
    
    # Define the goal amount and the amount raised after the first 3 hours
    goal_amount = 6300
    first_three_hours = 3

    # Calculate the amount raised after the first 3 hours
    amount_after_first_three_hours = first_three_hours + 2100

    # Calculate the amount raised per hour
    amount_per_hour = amount_after_first_three_hours / first_three_hours

    # Display the amount raised per hour
    result = amount_per_hour
    return result

print(solution())