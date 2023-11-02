def solution():
    # Calculate the number of students in each age group
    under_11 = 45/3  # a third of the class is under 11 years
    above_11_below_13 = (2/5) * 45  # two-fifths of the class are above 11 but below 13 years
    over_13 = 45 - under_11 - above_11_below_13  # the remaining students are over 13 years

    # Calculate the number of students in the third group
    third_group = over_13
    result = third_group
    return result

print(solution())