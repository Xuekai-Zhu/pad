def solution():
    """There are 30 students in the general study hall and twice as many students in the biology hall as there are in the general study hall. If the number of students in the math hall is 3/5 times as many as the combined total number of students in the general study hall and the biology hall combined, calculate the total number of students in all the halls combined."""
    # Calculate the number of students in the biology hall
    biology_students = 30 * 2

    # Calculate the combined total number of students in the general study hall and the biology hall
    general_biology_total = 30 + biology_students

    # Calculate the number of students in the math hall
    math_students = general_biology_total * (3/5)

    # Calculate the total number of students in all the halls combined
    total_students = general_biology_total + math_students

    # Display the total number of students
    result = total_students
    return result

print(solution())