def solution():
    # Calculate the total number of hot dog buns
    total_buns = 30 * 8

    # Calculate the number of students
    num_students = 4 * 30

    # Divide the total number of buns by the number of students to find how many each student can get
    buns_per_student = total_buns / num_students
    result = buns_per_student
    return result

print(solution())