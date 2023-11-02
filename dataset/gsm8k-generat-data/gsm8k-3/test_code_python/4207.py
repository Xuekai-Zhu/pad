def solution():
    """Mitzel spent 35% of her allowance. If she spent $14, how much money is left in her allowance?"""
    # Define the percentage of allowance that Mitzel spent
    SPENT_PERCENTAGE = 35

    # Define the amount Mitzel spent
    spent = 14

    # Calculate the total allowance
    total_allowance = spent / (SPENT_PERCENTAGE / 100)

    # Calculate the amount of money left in Mitzel's allowance
    remaining = total_allowance - spent

    # Display the amount of money left in Mitzel's allowance
    result = remaining
    return result

print(solution())