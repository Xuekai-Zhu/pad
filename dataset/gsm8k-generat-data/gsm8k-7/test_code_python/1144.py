def solution():
    younger_brother_age = 5
    older_brother_age = younger_brother_age * 3  # 3 times younger brother's age

    michael_age = (older_brother_age / 2) - 1  # Michael's age a year ago

    oldest_brother_age = 2 * michael_age + 1  # Oldest brother's age now

    total_age = michael_age + older_brother_age + younger_brother_age
    result = total_age
    return result

print(solution())