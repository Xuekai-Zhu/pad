def solution():
    younger_brother_age = 5  # The younger brother is 5 years old
    older_brother_age = 3 * younger_brother_age  # The older brother is 3 times as old as the younger brother
    michael_age = (older_brother_age / 2) - 1  # Michael's age when he was a year younger

    # Calculate the combined age of all three brothers
    combined_age = younger_brother_age + older_brother_age + michael_age
    result = combined_age
    return result

print(solution())