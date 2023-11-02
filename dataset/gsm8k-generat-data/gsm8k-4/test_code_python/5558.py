def solution():
    """The ratio of boys to girls in a math class is 5:8. How many girls are in the class if the total number of students in the class is 260?"""
    # Define the ratio of boys to girls
    boy_to_girl_ratio = 5/8

    # Define the total number of students
    total_students = 260

    # Calculate the number of girls in the class
    girls = total_students / (boy_to_girl_ratio + 1) * boy_to_girl_ratio

    # Round the number of girls to the nearest whole number
    girls = round(girls)

    # Return the number of girls
    result = girls
    return result

print(solution())