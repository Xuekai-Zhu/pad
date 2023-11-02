def solution():
    cracker_calories = 15
    cookie_calories = 50
    crackers_needed = (500 - (7 * cookie_calories)) / cracker_calories
    result = crackers_needed
    return result

print(solution())