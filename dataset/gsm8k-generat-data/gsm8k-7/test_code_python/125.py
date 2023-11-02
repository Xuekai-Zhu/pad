def solution():
    growth_rate = 3
    current_height = 20
    num_years = 10

    # Calculate the total growth in inches after 10 years
    total_growth = growth_rate * num_years

    # Calculate Haley's height in inches after 10 years
    new_height = current_height + total_growth
    result = new_height
    return result

print(solution())