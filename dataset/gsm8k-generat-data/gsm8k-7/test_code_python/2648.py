def solution():
    total_ratio = 4 + 3 + 7  # calculate total ratio
    total_age = 126  # given total age
    halima_ratio = 4 / total_ratio  # calculate Halima's ratio
    beckham_ratio = 3 / total_ratio  # calculate Beckham's ratio

    # use ratios to calculate age difference between Halima and Beckham
    age_difference = (halima_ratio * total_age) - (beckham_ratio * total_age)

    result = age_difference
    return result

print(solution())