def solution():
    """The ratio of boys to girls in a classroom is 3:5. If there are 4 more girls than boys, how many students are in the classroom?"""
    # Define the ratio of boys to girls
    boy_to_girl_ratio = 3/5

    # Set up the equation for the number of boys and girls
    # Let x be the number of boys
    # Then x+4 is the number of girls
    # We can set up the equation based on the ratio
    # x / (x+4) = 3/5
    x = 12

    # Calculate the total number of students
    total_students = x + (x+4)

    # Return the result
    result = total_students
    return result

print(solution())