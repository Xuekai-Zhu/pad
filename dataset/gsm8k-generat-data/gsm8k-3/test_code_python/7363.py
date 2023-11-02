def solution():
    """A class composed of 12 girls and 10 boys was sent to the library for their reading class. Their teacher found out that only 5/6 of the girls and 4/5 of the boys are reading. How many students are not reading?"""
    # Calculate the number of girls who are reading
    girls_reading = 5/6 * 12

    # Calculate the number of boys who are reading
    boys_reading = 4/5 * 10

    # Calculate the total number of students who are reading
    total_reading = girls_reading + boys_reading

    # Calculate the total number of students who are not reading
    total_not_reading = 22 - total_reading

    # Display the total number of students who are not reading
    result = total_not_reading
    return result

print(solution())