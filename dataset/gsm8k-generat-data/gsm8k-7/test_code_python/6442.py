def solution():
    num_buns_per_package = 8
    total_num_buns = 30 * num_buns_per_package
    num_students = 4 * 30

    # Calculate the number of buns each student can get
    num_buns_per_student = total_num_buns / num_students
    result = num_buns_per_student
    return result

print(solution())