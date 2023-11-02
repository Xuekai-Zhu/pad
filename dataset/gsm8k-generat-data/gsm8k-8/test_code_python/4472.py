def solution():
    # Calculate the number of calories Jimmy has consumed from the cookies
    cookies_calories = 7 * 50

    # Calculate the remaining number of calories Jimmy needs to consume
    remaining_calories = 500 - cookies_calories

    # Calculate the number of crackers Jimmy needs to eat to consume the remaining calories
    crackers_calories = 15
    crackers_needed = remaining_calories / crackers_calories
    result = crackers_needed
    return result

print(solution())