def solution():
    """There are 30 students in the general study hall and twice as many students in the biology hall as there are in the general study hall. If the number of students in the math hall is 3/5 times as many as the combined total number of students in the general study hall and the biology hall combined, calculate the total number of students in all the halls combined."""
    # Define the number of students in the general study hall
    general_students = 30

    # Define the number of students in the biology hall
    biology_students = general_students * 2

    # Define the total number of students in the general study hall and the biology hall combined
    gen_bio_total = general_students + biology_students

    # Define the number of students in the math hall
    math_students = 3/5 * gen_bio_total

    # Calculate the total number of students in all the halls
    total_students = general_students + biology_students + math_students

    # return the result
    result = total_students
    return result

print(solution())