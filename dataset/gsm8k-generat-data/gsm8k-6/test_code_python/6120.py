def solution():
    # Calculate the number of students who like the color blue
    blue_students = int(0.3 * 200)

    # Calculate the number of students who don't like the color blue
    remaining_students = 200 - blue_students

    # Calculate the number of students who like the color red
    red_students = int(0.4 * remaining_students)

    # Calculate the number of students who like the color yellow
    yellow_students = remaining_students - red_students

    # Calculate the combined number of students who like the color yellow and the color blue
    combined_students = blue_students + yellow_students
    result = combined_students
    return result

print(solution())