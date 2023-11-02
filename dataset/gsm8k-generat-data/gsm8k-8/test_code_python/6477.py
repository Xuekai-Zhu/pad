def solution():
    # Define the variables
    days_remaining = 3
    target_amount = 1000
    current_amount = 300 + 40

    # Calculate the amount that still needs to be raised
    remaining_amount = target_amount - current_amount

    # Calculate how much he needs to raise each day
    amount_per_day = remaining_amount / days_remaining

    # Calculate how many houses he needs to visit each day
    houses_per_day = amount_per_day / 2.5

    result = houses_per_day
    return result

print(solution())