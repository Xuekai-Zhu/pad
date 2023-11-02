def solution():
    total_students = 45
    under_11_ratio = 1/3
    above_11_below_13_ratio = 2/5

    # Calculate the number of students under 11 years old
    under_11 = total_students * under_11_ratio

    # Calculate the number of students above 11 but below 13 years old
    above_11_below_13 = total_students * above_11_below_13_ratio

    # Calculate the number of students 13 years old and above
    above_13 = total_students - under_11 - above_11_below_13

    result = above_13
    return result

print(solution())