def solution():
    amount_spent = 14  # Mitzel spent $14
    percent_spent = 0.35  # Mitzel spent 35% of her allowance

    # Calculate the total allowance
    total_allowance = amount_spent / percent_spent

    # Calculate how much money is left in her allowance
    money_left = total_allowance - amount_spent
    result = money_left
    return result

print(solution())