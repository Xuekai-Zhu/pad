def solution():
    third_school_students = 200
    second_school_students = third_school_students + 40
    first_school_students = 2 * second_school_students

    # Calculate the total number of students who shook the mayor's hand
    total_students = first_school_students + second_school_students + third_school_students
    result = total_students
    return result

print(solution())