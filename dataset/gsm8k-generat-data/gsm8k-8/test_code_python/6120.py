def solution():
    # Calculate the number of students who like blue
    blue_students = 0.3 * 200

    # Calculate the number of students who don't like blue
    non_blue_students = 200 - blue_students

    # Calculate the number of students who like red
    red_students = 0.4 * non_blue_students

    # Calculate the number of students who like yellow
    yellow_students = non_blue_students - red_students

    # Calculate the total number of students who like blue and yellow
    total_students = blue_students + yellow_students
    result = total_students
    return result

print(solution())