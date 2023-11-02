def solution():
    # Calculate the current revenue per year
    current_revenue_per_year = 4000 * 12

    # Calculate the additional revenue needed per year
    additional_revenue_per_year = 60000 - current_revenue_per_year

    # Calculate the additional revenue needed per month
    additional_revenue_per_month = additional_revenue_per_year / 12
    result = additional_revenue_per_month
    return result

print(solution())