def solution():
    """The difference between the number of boys and girls in a tree planting event is 400. If there are 600 boys at the event, and the number of girls is more than the number of boys, what's 60% of the total number of boys and girls at the event?"""
    # Define the number of boys and the difference between the number of boys and girls
    boys = 600
    diff = 400

    # Calculate the number of girls
    girls = boys + diff

    # Calculate the total number of students
    total_students = boys + girls

    # Calculate 60% of the total number of students
    sixty_percent = 0.6 * total_students

    # Return the result
    result = sixty_percent
    return result

print(solution())