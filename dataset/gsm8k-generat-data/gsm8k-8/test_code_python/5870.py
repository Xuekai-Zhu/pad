def solution():
    # Calculate the number of orange harvests in a year
    orange_harvests_per_year = 12 / 2

    # Calculate the total revenue from orange sales
    orange_revenue_per_year = orange_harvests_per_year * 50

    # Calculate the number of apple harvests in a year
    apple_harvests_per_year = 12 / 3

    # Calculate the total revenue from apple sales
    apple_revenue_per_year = apple_harvests_per_year * 30

    # Calculate the total revenue from both orange and apple sales
    total_revenue_per_year = orange_revenue_per_year + apple_revenue_per_year
    result = total_revenue_per_year
    return result

print(solution())