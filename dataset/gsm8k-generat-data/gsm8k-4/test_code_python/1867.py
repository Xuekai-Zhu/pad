def solution():
    """There are 20 students in a class. Only one-fourth of the students stayed in the classroom while the rest went to the playground. Of those who went to the playground, one-third are boys. How many girls are there on the playground from this class?"""
    # Define the total number of students in the class
    total_students = 20

    # Calculate the number of students who stayed in the classroom
    classroom_students = total_students // 4

    # Calculate the number of students who went to the playground
    playground_students = total_students - classroom_students

    # Calculate the number of boys on the playground
    playground_boys = playground_students // 3

    # Calculate the number of girls on the playground
    playground_girls = playground_students - playground_boys

    # Return the result
    result = playground_girls
    return result

print(solution())