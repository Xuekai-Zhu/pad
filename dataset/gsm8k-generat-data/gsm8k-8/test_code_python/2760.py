def solution():
    # Define Joel's age and his dad's age
    joel_age = 5
    dad_age = 32

    # Find the age difference between Joel and his dad
    age_diff = dad_age - joel_age

    # Find the age at which dad will be twice as old as Joel
    twice_age_diff = age_diff * 2

    # Add the age difference to Joel's current age to find the age at which his dad will be twice as old
    age_when_dad_is_twice = joel_age + twice_age_diff

    result = age_when_dad_is_twice
    return result

print(solution())