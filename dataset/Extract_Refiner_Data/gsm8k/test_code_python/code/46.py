def solution():
    
    # Define the number of eggs produced per day and the price per dozen
    eggs_per_day = 252
    price_per_dozen = 2

    # Calculate the total number of eggs produced per week
    eggs_per_week = eggs_per_day * 7

    # Calculate the total number of dozens of eggs produced per week
    dozens_per_week = eggs_per_week / 12

    # Calculate the total revenue from selling the eggs per week
    total_revenue = dozens_per_week * price_per_dozen

    # return the result
    result = total_revenue
    return result

print(solution())