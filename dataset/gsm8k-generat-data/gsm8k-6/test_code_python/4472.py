def solution():
    # Calculate the number of calories Jimmy consumed from the cookies
    cookie_calories = 50 * 7

    # Calculate the remaining calories Jimmy needs to consume from crackers
    remaining_calories = 500 - cookie_calories

    # Calculate the number of crackers Jimmy needs to eat
    crackers_needed = remaining_calories // 15  # each cracker contains 15 calories

    result = crackers_needed
    return result

print(solution())