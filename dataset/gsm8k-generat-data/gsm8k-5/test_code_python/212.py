def solution():
    years_to_practice = 8  # Randy wants to become an expert before he is 20, so he has 8 years to practice
    weeks_in_year = 52  # There are 52 weeks in a year
    weeks_off = 2  # Randy takes 2 weeks off for vacation each year
    weeks_to_practice = (weeks_in_year - weeks_off) * 5  # Randy only practices Monday-Friday

    # Calculate the total number of hours Randy needs to practice
    total_hours_needed = 10000
    total_weeks_of_practice = years_to_practice * weeks_to_practice
    hours_per_week = (total_hours_needed / total_weeks_of_practice)
    hours_per_day = hours_per_week / 5  # Divide by 5 to get hours per day

    result = hours_per_day
    return result

print(solution())