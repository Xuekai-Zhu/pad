def solution():
    # Calculate Rick's age
    rick_age = 15

    # Calculate the oldest brother's age
    oldest_brother_age = 2 * rick_age

    # Calculate the middle brother's age
    middle_brother_age = oldest_brother_age / 3

    # Calculate the smallest brother's age
    smallest_brother_age = middle_brother_age / 2

    # Calculate the youngest brother's age
    youngest_brother_age = smallest_brother_age - 2
    result = youngest_brother_age
    return result

print(solution())