def solution():
    # Calculate the number of students who answered green
    green_students = 30 / 2

    # Calculate the number of girls who answered pink
    pink_girls = 18 / 3

    # Calculate the number of students who answered yellow
    yellow_students = 30 - green_students - pink_girls

    result = yellow_students
    return result

print(solution())