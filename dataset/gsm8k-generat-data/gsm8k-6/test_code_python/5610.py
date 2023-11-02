def solution():
    # Calculate the ages of Rick's siblings
    oldest_brother_age = 2 * 15  # oldest brother is twice Rick's age
    middle_brother_age = oldest_brother_age / 3  # middle brother is a third of the oldest brother's age
    smallest_brother_age = middle_brother_age / 2  # smallest brother is half the middle brother's age
    youngest_brother_age = smallest_brother_age - 2  # youngest brother is 2 years younger than the smallest brother
    result = youngest_brother_age
    return result

print(solution())