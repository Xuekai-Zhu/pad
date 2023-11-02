def solution():
    rahim_age_now = 6  # Rahim is 6 years old now
    andy_age_in_5_years = rahim_age_now * 2  # In 5 years, Andy will be twice as old as Rahim is now
    andy_age_now = andy_age_in_5_years - 5  # Calculate Andy's current age

    # Calculate the age difference between Andy and Rahim
    age_difference = andy_age_now - rahim_age_now
    result = age_difference
    return result

print(solution())