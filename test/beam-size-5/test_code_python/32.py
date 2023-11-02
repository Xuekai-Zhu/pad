def solution():
    yogurts_per_day = 2
    sale_price = 5.0
    days = 30

    # Calculate the total number of yogurts Terry eats over 30 days
    total_yogurts = yogurts_per_day * days

    # Calculate the total cost of yogurts Terry eats over 30 days
    total_cost = total_yogurts * sale_price
    result = total_cost
    return result

print(solution())