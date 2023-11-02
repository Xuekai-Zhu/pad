def solution():
    total_years = 8  # Randy wants to become an expert before he turns 20, so he has 8 years of practice
    weeks_in_year = 52  # Assuming 52 weeks in a year
    weeks_of_vacation = 2 * 8  # Randy will take 2 weeks off each year for vacation
    weeks_of_practice = (weeks_in_year - weeks_of_vacation) * 5  # Assuming Randy practices Monday-Friday only
    hours_of_practice_per_week = 5  # Assuming Randy practices for 5 hours per day
    total_hours_of_practice = weeks_of_practice * hours_of_practice_per_week * total_years
    result = total_hours_of_practice
    return result

print(solution())