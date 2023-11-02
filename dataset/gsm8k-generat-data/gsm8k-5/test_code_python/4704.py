def solution():
    weeks_first_country = 2
    weeks_second_country = weeks_first_country * 2
    weeks_third_country = weeks_first_country * 2
    total_weeks = weeks_first_country + weeks_second_country + weeks_third_country
    result = total_weeks
    return result * 7 # Convert to days

print(solution())