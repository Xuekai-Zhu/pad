def solution():
    starting_rate = 10  # Cary starts working for $10/hour
    first_year_rate = starting_rate * 1.2  # Cary gets a 20% raise in her first year
    second_year_rate = first_year_rate * 0.75  # Her pay is then cut to 75% of what she made in her first year

    # Calculate Cary's current rate of pay
    current_rate = second_year_rate
    result = current_rate
    return result

print(solution())