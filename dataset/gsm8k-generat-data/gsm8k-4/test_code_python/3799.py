def solution():
    """In four years, Suzy will be twice Mary's age then. If Suzy is 20 now, how old is Mary?"""
    # Define the current age of Suzy and the age difference between Suzy and Mary
    suzy_age = 20
    age_diff = suzy_age // 2

    # Calculate Mary's current age
    mary_age = suzy_age - age_diff

    # Return Mary's current age
    result = mary_age
    return result

print(solution())