def solution():
    hans_age = 15  # Hans is currently 15 years old
    josiah_age = hans_age * 3  # Josiah is three times as old as Hans

    # In three years, the age of Hans will be:
    hans_age_in_3_years = hans_age + 3
    
    # In three years, the age of Josiah will be:
    josiah_age_in_3_years = josiah_age + 3
    
    # The sum of their ages in three years will be:
    sum_of_ages_in_3_years = hans_age_in_3_years + josiah_age_in_3_years
    
    result = sum_of_ages_in_3_years
    return result

print(solution())