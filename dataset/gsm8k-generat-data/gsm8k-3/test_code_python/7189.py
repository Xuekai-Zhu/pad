def solution():
    """There are 11 boys and 13 girls in a class. If 1 boy is added to the class, what percentage of the class are girls?"""
    # Define the initial number of boys and girls
    initial_boys = 11
    initial_girls = 13

    # Add one boy to the class
    new_boys = initial_boys + 1

    # Calculate the total number of students in the class
    total_students = new_boys + initial_girls

    # Calculate the percentage of girls in the class
    girls_percentage = (initial_girls / total_students) * 100

    # Display the percentage of girls in the class
    result = girls_percentage
    return result

print(solution())