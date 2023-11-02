def solution():
    """The ratio of boys to girls in a math class is 5:8. How many girls are in the class if the total number of students in the class is 260?"""
    # Define the ratio of boys to girls
    BOYS_TO_GIRLS = 5/8

    # Define the total number of students
    total_students = 260

    # Calculate the number of girls in the class
    girls = total_students/(1+BOYS_TO_GIRLS)
    
    # Display the number of girls in the class
    result = int(girls)
    return result

print(solution())