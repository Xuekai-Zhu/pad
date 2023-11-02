def solution():
    borrowed_amount = 1200
    interest_rate = 0.1  # 10% interest

    # Calculate the amount of interest
    interest_amount = borrowed_amount * interest_rate

    # Calculate the total amount to be paid back
    total_amount = borrowed_amount + interest_amount
    result = total_amount
    return result

print(solution())