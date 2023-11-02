def solution():
    # Calculate the revenue from oranges
    oranges_per_year = 12/2  # Keaton can harvest oranges every 2 months, so he can harvest them 6 times a year
    revenue_oranges = oranges_per_year * 50  # $50 per harvest

    # Calculate the revenue from apples
    apples_per_year = 12/3  # Keaton can harvest apples every 3 months, so he can harvest them 4 times a year
    revenue_apples = apples_per_year * 30  # $30 per harvest

    # Calculate the total revenue Keaton can earn every year
    total_revenue = revenue_oranges + revenue_apples
    result = total_revenue
    return result

print(solution())