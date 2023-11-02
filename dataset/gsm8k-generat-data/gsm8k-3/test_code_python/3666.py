def solution():
    """Jordan's dog, Max, was born on the same day that Luka turned 4 years old.  Luka is exactly 2 years older than is Aubrey.  On Aubrey's 8th birthday, how many years old was Jordan's dog, Max?"""
    # Determine Luka's age on Aubrey's 8th birthday
    luka_age = 8 + 2

    # Determine Max's age on Luka's 4th birthday
    max_age = luka_age - 4

    # Determine Max's age on Aubrey's 8th birthday
    max_age_on_aubrey_birthday = max_age + 8

    # Display Max's age on Aubrey's 8th birthday
    result = max_age_on_aubrey_birthday
    return result

print(solution())