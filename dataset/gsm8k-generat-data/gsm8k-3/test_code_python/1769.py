def solution():
    """Miss Molly surveyed her class of 30 students about their favorite color. Half of the class answered green, one-third of the girls answered pink, and the rest of the class answered yellow. If there are 18 girls in the class, how many students like yellow best?"""
    # Define the total number of students in the class
    total_students = 30

    # Calculate the number of students who answered green
    green_students = total_students / 2

    # Calculate the number of girls who answered pink
    girls = 18
    pink_girls = girls / 3

    # Calculate the number of students who like yellow
    yellow_students = total_students - green_students - pink_girls

    # Display the number of students who like yellow
    result = yellow_students
    return result

print(solution())