def solution():
    """In the engineering department, 70% of the students are men and 180 are women. How many men are there?"""
    # Define the percentage of men in the engineering department and the number of women
    MEN_PERCENTAGE = 0.7
    WOMEN_NUMBER = 180

    # Calculate the total number of students in the engineering department
    total_students = WOMEN_NUMBER / (1 - MEN_PERCENTAGE)

    # Calculate the number of men in the engineering department
    men_number = total_students * MEN_PERCENTAGE

    # Display the number of men in the engineering department
    result = men_number
    return result

print(solution())