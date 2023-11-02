def solution():
    """Mitzel spent 35% of her allowance. If she spent $14, how much money is left in her allowance?"""
    # Define the percentage of allowance Mitzel spent and the amount she spent
    spent_percentage = 35
    spent_amount = 14

    # Calculate the total allowance
    total_allowance = spent_amount / (spent_percentage / 100)

    # Calculate the amount of money left in the allowance
    remaining_money = total_allowance - spent_amount

    # return the result
    result = remaining_money
    return result

print(solution())