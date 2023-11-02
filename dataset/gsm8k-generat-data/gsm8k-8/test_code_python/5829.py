def solution():
    # Calculate the number of black and white shirts sold
    black_shirts = 200 / 2
    white_shirts = 200 / 2

    # Calculate the total revenue from black and white shirts
    black_revenue = black_shirts * 30
    white_revenue = white_shirts * 25
    total_revenue = black_revenue + white_revenue

    # Calculate the revenue per minute
    revenue_per_minute = total_revenue / 25
    result = revenue_per_minute
    return result

print(solution())