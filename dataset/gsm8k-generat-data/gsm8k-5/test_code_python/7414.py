def solution():
    total_students = 45  # Musa has a class of 45 students

    # Calculate the number of students under 11 years
    under_11 = total_students / 3
    # Calculate the number of students above 11 years but under 13 years
    above_11_under_13 = (2 / 5) * total_students
    # Calculate the number of students in the third group (13 years and above)
    third_group = total_students - under_11 - above_11_under_13
    result = third_group
    return result

print(solution())