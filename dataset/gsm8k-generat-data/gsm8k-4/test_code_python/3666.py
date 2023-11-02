def solution():
    """Jordan's dog, Max, was born on the same day that Luka turned 4 years old. Luka is exactly 2 years older than is Aubrey. On Aubrey's 8th birthday, how many years old was Jordan's dog, Max?"""
    # Define Luka's age and Aubrey's age
    luka_age = 8 - 4
    aubrey_age = luka_age - 2

    # Define Max's age as the difference between Aubrey's age and Max's age when Max was born
    max_age = 8 - luka_age

    # Return Max's age on Aubrey's 8th birthday
    result = max_age + aubrey_age
    return result

print(solution())