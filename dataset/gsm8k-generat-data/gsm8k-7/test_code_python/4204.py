def solution():
    initial_height = 50  # inches
    growth_rate = 6      # inches per year
    num_years = 4        # 4 years from age 8 to age 12

    # Calculate the total growth in inches over the 4 years
    total_growth = growth_rate * num_years

    # Calculate the final height in inches
    final_height = initial_height + total_growth
    result = final_height
    return result

print(solution())