def solution():
    """There are 20 students in a class. Only one-fourth of the students stayed in the classroom while the rest went to the playground. Of those who went to the playground, one-third are boys. How many girls are there on the playground from this class?"""
    # Define the total number of students
    total_students = 20

    # Calculate the number of students who went to the playground
    playground_students = total_students - total_students//4

    # Calculate the number of boys on the playground
    boys_on_playground = playground_students//3

    # Calculate the number of girls on the playground
    girls_on_playground = playground_students - boys_on_playground

    # Display the number of girls on the playground
    result = girls_on_playground
    return result

print(solution())