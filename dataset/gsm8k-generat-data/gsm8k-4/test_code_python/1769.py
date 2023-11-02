def solution():
    """Miss Molly surveyed her class of 30 students about their favorite color. Half of the class answered green, one-third of the girls answered pink, and the rest of the class answered yellow. If there are 18 girls in the class, how many students like yellow best?"""
    # Define the total number of students and the number of girls
    total_students = 30
    girls = 18

    # Calculate the number of students who answered green
    green_students = total_students // 2

    # Calculate the number of girls who answered pink
    pink_girls = girls // 3

    # Calculate the number of students who answered yellow
    yellow_students = total_students - green_students - girls

    # return the result
    result = yellow_students
    return result

print(solution())