def solution():
    # Define the number of bowls, losses, and fees
    num_bowls = 638
    num_loss = 12
    num_broken = 15
    fee = 100

    # Calculate the number of bowls delivered safely
    num_safe = num_bowls - num_loss - num_broken

    # Calculate the amount earned from safe delivery
    safe_earnings = num_safe * 3

    # Calculate the amount lost from broken bowls
    lost_cost = num_broken * 4

    # Calculate the total earnings
    total_earnings = fee + safe_earnings - lost_cost
    result = total_earnings
    return result

print(solution())