def solution():
    """If 60% of the students at school are girls and the number of boys is 300, how many girls are at the school?"""
    # Define the percentage of girls at the school and the number of boys
    girls_percentage = 60
    boys = 300

    # Calculate the total number of students at the school
    total_students = (boys / (100 - girls_percentage)) * 100

    # Calculate the number of girls at the school
    girls = total_students - boys

    # Return the result
    result = girls
    return result

print(solution())