def solution():
    total_age = 17  # The current total of their ages is 17
    age_difference = 3  # Gabriel is 3 years younger than Frank

    # Set up two equations with two variables to solve for their ages
    # Let x be Frank's age and y be Gabriel's age
    # x + y = total_age
    # x - y = age_difference
    # Solve for x, which is Frank's age
    x = (total_age + age_difference) / 2
    result = x
    return result

print(solution())