def solution():
    # Calculate the amount of the 15% tip
    tip_15_percent = 42
    total_amount = tip_15_percent / 0.15  # Divide by 0.15 to get the total bill amount

    # Calculate the amount of a 20% tip
    tip_20_percent = total_amount * 0.20
    result = tip_20_percent
    return result

print(solution())