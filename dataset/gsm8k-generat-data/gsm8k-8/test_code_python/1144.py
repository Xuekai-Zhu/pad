def solution():
    # Calculate Michael's age when he was a year younger
    michael_age = 5 * 3 - 1

    # Calculate the oldest brother's age
    oldest_brother_age = 1 + 2 * michael_age

    # Calculate the combined age of all three brothers
    combined_age = michael_age + oldest_brother_age + 5
    result = combined_age
    return result

print(solution())