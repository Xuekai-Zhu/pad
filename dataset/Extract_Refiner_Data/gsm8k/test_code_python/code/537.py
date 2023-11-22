def solution():
    
    # Define the target savings and the number of days in April
    target_savings = 1120
    days_in_april = 30

    # Calculate the savings for each day in April
    savings_first_half = target_savings / (2**days_in_april)
    savings_second_half = savings_first_half * 2 ** (days_in_april / 2))

    # Display the savings for each day in April
    result = savings_second_half
    return result

print(solution())