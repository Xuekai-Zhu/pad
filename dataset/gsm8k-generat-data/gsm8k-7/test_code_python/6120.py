def solution():
    total_students = 200
    blue_percentage = 0.3
    red_percentage = 0.4

    # Calculate the number of students who like blue
    blue_students = total_students * blue_percentage

    # Calculate the number of students who don't like blue
    non_blue_students = total_students - blue_students

    # Calculate the number of students who like red
    red_students = non_blue_students * red_percentage

    # Calculate the number of students who like yellow
    yellow_students = non_blue_students - red_students

    # Calculate the combined number of students who like yellow and blue
    combined_students = blue_students + yellow_students
    result = combined_students
    return result

print(solution())