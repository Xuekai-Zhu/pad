def solution():
    years_to_chief = 8
    years_to_master_chief = int(years_to_chief * 1.25)
    years_to_retirement = 10

    # Calculate the total number of years in the military
    total_years = years_to_chief + years_to_master_chief + years_to_retirement

    # Add 18 (the age at which Jason joined) to get his retirement age
    retirement_age = 18 + total_years
    result = retirement_age
    return result

print(solution())