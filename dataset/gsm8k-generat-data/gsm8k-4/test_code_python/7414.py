def solution():
    """Musa is the class teacher of a class of 45 students. He wants to split them into three groups by age. If a third of the class is under 11 years, and two-fifths are above 11 but under 13, how many students will be in the third group (13 years and above)?"""
    # Define the total number of students
    total_students = 45

    # Calculate the number of students under 11 years
    under_11 = total_students // 3

    # Calculate the number of students above 11 but under 13 years
    above_11_under_13 = total_students * 2 // 5

    # Calculate the number of students in the third group (13 years and above)
    third_group = total_students - under_11 - above_11_under_13

    # return the result
    result = third_group
    return result

print(solution())