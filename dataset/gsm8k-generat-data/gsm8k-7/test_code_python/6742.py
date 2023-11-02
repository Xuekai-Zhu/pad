def solution():
    initial_length = 4  # inches
    growth_rate = 2  # doubling in length
    age_in_months = 4

    # Calculate the length after the first 2 weeks of growth
    length_in_weeks = 2
    weeks_per_month = 4  # assuming 4 weeks in a month
    length_after_2_weeks = initial_length * growth_rate

    # Calculate the current length
    current_length = length_after_2_weeks * growth_rate ** (age_in_months * weeks_per_month - length_in_weeks)
    result = current_length
    return result

print(solution())