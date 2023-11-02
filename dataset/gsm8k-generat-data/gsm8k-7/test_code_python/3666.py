def solution():
    luka_age = 4 + 2  # Luka is 2 years older than Aubrey
    aubrey_age_on_max_birthday = 8 + 4  # Aubrey is 8 years old on Max's birthday

    # Calculate the difference between Aubrey's age and Luka's age on Max's birthday
    age_difference = luka_age - aubrey_age_on_max_birthday

    # Subtract the age difference from Max's age on Aubrey's 8th birthday to find Max's age on Aubrey's 8th birthday
    max_age_on_aubrey_birthday = aubrey_age_on_max_birthday - age_difference
    result = max_age_on_aubrey_birthday
    return result

print(solution())