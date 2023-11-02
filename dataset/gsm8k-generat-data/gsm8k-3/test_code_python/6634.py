def solution():
    """If 60% of the students at school are girls and the number of boys is 300, how many girls are at the school?"""
    # Define the percentage of girls at school and the number of boys
    GIRL_PERCENTAGE = 60
    BOYS = 300

    # Calculate the total number of students at school
    total_students = (100 / (100 - GIRL_PERCENTAGE)) * BOYS

    # Calculate the number of girls at school
    girls = total_students - BOYS

    # Display the number of girls at school
    result = girls
    return result

print(solution())