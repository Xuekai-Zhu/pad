def solution():
    heath_age = 16
    years_to_add = 5

    # Calculate the age difference between Heath and Jude in 5 years
    age_difference = heath_age * 3 - heath_age

    # Calculate Jude's age by subtracting the age difference from Heath's age in 5 years
    jude_age = heath_age + years_to_add - age_difference
    result = jude_age
    return result

print(solution())