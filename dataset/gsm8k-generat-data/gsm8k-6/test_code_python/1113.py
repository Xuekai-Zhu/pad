def solution():
    younger_brother_age = 10  # given younger brother's age
    brother_was_2 = younger_brother_age - 8  # younger brother was 2 years old 8 years ago
    viggo_age = 10 + 2 * brother_was_2  # given Viggo's age is 10 more than twice his younger brother's age
    total_age = viggo_age + younger_brother_age  # sum of their current ages
    result = total_age
    return result

print(solution())