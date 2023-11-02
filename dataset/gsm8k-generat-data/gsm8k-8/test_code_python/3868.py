def solution():
    # Define the original amount of liquid in the barrel
    original_amount = 220

    # Calculate the amount that was lost
    lost_amount = 0.1 * original_amount

    # Calculate the amount remaining in the barrel
    remaining_amount = original_amount - lost_amount

    result = remaining_amount
    return result

print(solution())