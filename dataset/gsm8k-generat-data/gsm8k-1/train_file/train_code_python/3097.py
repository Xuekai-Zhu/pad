def solution():
    """The ages of three brothers are consecutive integers with the sum of 96. How old is the youngest brother?"""
    sum_ages = 96
    middle_age = sum_ages // 3
    youngest_age = middle_age - 1
    result = youngest_age
    return result

print(solution())