def solution():
    # Define the sum of their ages and the age difference
    age_sum = 7
    age_diff = 1

    # Use algebra to solve for Mario's age
    # Let M be Mario's age and m be Maria's age
    # Then we know M + m = age_sum and M = m + age_diff
    # Substitute the second equation into the first to get: (m + age_diff) + m = age_sum
    # Simplifying gives: 2m + age_diff = age_sum
    # Substituting in the given values gives: 2m + 1 = 7
    # Solving for m gives: m = 3
    # Then we can find Mario's age by adding the age difference: M = m + age_diff = 3 + 1 = 4
    mario_age = 4
    result = mario_age
    return result

print(solution())