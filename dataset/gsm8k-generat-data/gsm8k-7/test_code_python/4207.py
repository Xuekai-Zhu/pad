def solution():
    percentage_spent = 0.35
    amount_spent = 14

    # Calculate the total allowance
    total_allowance = amount_spent / percentage_spent

    # Calculate the amount of money left in the allowance
    money_left = total_allowance - amount_spent
    result = money_left
    return result

print(solution())