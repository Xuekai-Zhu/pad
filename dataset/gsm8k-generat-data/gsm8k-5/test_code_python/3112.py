def solution():
    third_school_students = 200  # The third school had 200 students
    second_school_students = third_school_students + 40  # The second school had 40 more students than the third school
    first_school_students = 2 * second_school_students  # The first school had twice as many students as the second school

    # Calculate the total number of students who shook the mayor's hand
    total_students = first_school_students + second_school_students + third_school_students
    result = total_students
    return result

print(solution())