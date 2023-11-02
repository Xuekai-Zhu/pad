def solution():
    final_height = 80
    initial_height = 20
    num_months = 12

    # Calculate the total growth of the plant in feet
    total_growth = final_height - initial_height

    # Calculate the monthly growth rate in feet
    growth_rate_per_month = total_growth / num_months
    result = growth_rate_per_month
    return result

print(solution())