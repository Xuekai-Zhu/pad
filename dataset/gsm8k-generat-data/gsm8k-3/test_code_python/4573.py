def solution():
    """The ratio of boys to girls in a classroom is 3:5. If there are 4 more girls than boys, how many students are in the classroom?"""
    # Define the ratio of boys to girls and the difference in number of boys and girls
    ratio = 3/5
    diff = 4

    # Set up a system of equations to solve for the number of boys and girls
    # Let x be the number of boys, then the number of girls is 5/3 times x, or 5x/3
    # The number of girls is also x + 4
    # Therefore, 5x/3 = x + 4
    # Solving for x, we get x = 12
    # Therefore, the number of girls is 5x/3 = 20

    # Calculate the total number of students
    total_students = 12 + 20

    # Display the total number of students
    result = total_students
    return result

print(solution())