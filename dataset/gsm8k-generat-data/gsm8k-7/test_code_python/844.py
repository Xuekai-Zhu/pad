def solution():
    current_age_rahim = 6
    age_difference = 2   # In 5 years, Andy will be twice as old as Rahim is now

    # Calculate Andy's age in 5 years
    age_in_5_years = age_difference * current_age_rahim

    # Calculate Andy's current age
    current_age_andy = age_in_5_years - 5

    # Calculate the age difference between Andy and Rahim
    age_difference_now = current_age_andy - current_age_rahim
    result = age_difference_now
    return result

print(solution())