def solution():
    # Calculate the total amount to be borrowed including interest
    total_borrowed = 100 * 12  # $100.00 per month for 12 months
    interest = 0.1 * total_borrowed  # 10% interest fee
    total_amount = total_borrowed + interest

    result = total_amount
    return result

print(solution())