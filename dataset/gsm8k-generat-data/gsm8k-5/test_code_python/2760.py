def solution():
    dad_age = 32
    joel_age = 5
    age_diff = dad_age - joel_age  # Calculate the age difference between Joel and his dad

    # Calculate the number of years until Joel's dad is twice as old as him
    years_until_twice_as_old = age_diff

    # Calculate Joel's age when his dad is twice as old as him
    joel_age_when_dad_is_twice = joel_age + years_until_twice_as_old

    result = joel_age_when_dad_is_twice
    return result

print(solution())