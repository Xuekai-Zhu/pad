def solution():
    # Calculate Michael's age
    michael_age = 5 + (1/3) * (2 * (michael_age - 1) + 1)

    # Calculate the age of Michael's oldest brother
    oldest_brother_age = 2 * (michael_age - 1) + 1

    # Calculate the combined age of Michael and his brothers
    combined_age = michael_age + oldest_brother_age + 5
    result = combined_age
    return result

print(solution())