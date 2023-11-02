def solution():
    """Out of the 150 students, 60% are girls and the rest are boys. Only 1/3 of the boys joined varsity clubs. How many of the boys did not join varsity clubs?"""
    # Define the total number of students and the percentage of girls
    total_students = 150
    girls_percentage = 0.6

    # Calculate the number of girls and boys
    girls = total_students * girls_percentage
    boys = total_students - girls

    # Calculate the number of boys who joined varsity clubs
    varsity_boys = boys / 3

    # Calculate the number of boys who did not join varsity clubs
    non_varsity_boys = boys - varsity_boys

    result = non_varsity_boys
    return result

print(solution())