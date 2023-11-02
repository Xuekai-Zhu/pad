def solution():
    total_students = 30  # Miss Molly has a class of 30 students
    girls = 18  # There are 18 girls in the class

    # Calculate the number of students who answered green
    green = total_students // 2

    # Calculate the number of girls who answered pink
    pink = girls // 3

    # Calculate the number of students who answered yellow
    yellow = total_students - green - pink - girls

    result = yellow
    return result

print(solution())