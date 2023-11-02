def solution():
    current_chickens = 550
    increase_per_year = 150
    num_years = 9

    # Calculate the total increase in number of chickens after 9 years
    total_increase = increase_per_year * num_years

    # Calculate the number of chickens after 9 years
    total_chickens = current_chickens + total_increase
    result = total_chickens
    return result

print(solution())