def solution():
    john_age = 10
    sister_age = 2 * john_age  # Sister is twice John's age
    age_difference = sister_age - john_age  # Find difference between their ages

    # When John is 50, how old will his sister be?
    sister_age_at_50 = 50 + age_difference

    result = sister_age_at_50
    return result

print(solution())