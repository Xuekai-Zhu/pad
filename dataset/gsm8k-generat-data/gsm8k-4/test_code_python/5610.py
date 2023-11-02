def solution():
    """Rick has just celebrated his 15th birthday. His oldest brother is twice his age, and his middle brother is a third of the oldest brother’s age. The smallest brother is half the middle brother’s age. If the youngest brother is 2 years younger than the smallest brother, how old, in years, is the youngest brother?"""
    # Define Rick's age
    rick_age = 15

    # Calculate the oldest brother's age
    oldest_brother_age = rick_age * 2

    # Calculate the middle brother's age
    middle_brother_age = oldest_brother_age / 3

    # Calculate the smallest brother's age
    smallest_brother_age = middle_brother_age / 2

    # Calculate the youngest brother's age
    youngest_brother_age = smallest_brother_age - 2

    result = youngest_brother_age
    return result

print(solution())