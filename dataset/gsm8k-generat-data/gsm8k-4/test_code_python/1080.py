def solution():
    """In the engineering department, 70% of the students are men and 180 are women. How many men are there?"""
    # Define the total number of students
    total_students = 100

    # Define the number of women
    women = 180

    # Calculate the percentage of men
    men_percentage = 70

    # Calculate the number of men
    men = (men_percentage / 100) * total_students - women

    # Return the result
    result = men
    return result

print(solution())