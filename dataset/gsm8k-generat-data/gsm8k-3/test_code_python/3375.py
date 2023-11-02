def solution():
    """Out of the 150 students, 60% are girls and the rest are boys. Only 1/3 of the boys joined varsity clubs. How many of the boys did not join varsity clubs?"""
    # Define the total number of students
    total_students = 150

    # Calculate the number of girls
    girls = int(total_students * 0.6)

    # Calculate the number of boys
    boys = total_students - girls

    # Calculate the number of boys who joined varsity clubs
    varsity_boys = int(boys * (1/3))

    # Calculate the number of boys who did not join varsity clubs
    non_varsity_boys = boys - varsity_boys

    # Display the number of boys who did not join varsity clubs
    result = non_varsity_boys
    return result

print(solution())