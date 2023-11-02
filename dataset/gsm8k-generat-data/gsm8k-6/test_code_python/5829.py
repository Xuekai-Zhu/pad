def solution():
    # Calculate the number of black and white t-shirts sold
    black_shirts = 200/2
    white_shirts = 200/2

    # Calculate the total revenue from the sale
    revenue = (black_shirts * 30) + (white_shirts * 25)

    # Calculate the revenue per minute
    revenue_per_minute = revenue / 25

    result = revenue_per_minute
    return result

print(solution())