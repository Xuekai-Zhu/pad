def solution():
    num_middle_school_students = 50

    # Calculate the number of elementary school students using the given ratio
    # 4x - 3 = number of elementary school students
    num_elem_school_students = 4*num_middle_school_students - 3

    # Calculate the total number of students
    total_students = num_middle_school_students + num_elem_school_students
    result = total_students
    return result

print(solution())