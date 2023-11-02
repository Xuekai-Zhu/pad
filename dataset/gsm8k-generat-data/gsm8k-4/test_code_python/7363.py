def solution():
    """A class composed of 12 girls and 10 boys was sent to the library for their reading class. Their teacher found out that only 5/6 of the girls and 4/5 of the boys are reading. How many students are not reading?"""
    # Define the number of girls and boys in the class
    num_girls = 12
    num_boys = 10

    # Calculate the number of girls and boys who are reading
    reading_girls = (5/6) * num_girls
    reading_boys = (4/5) * num_boys

    # Calculate the total number of students who are reading
    total_reading = reading_girls + reading_boys

    # Calculate the total number of students who are not reading
    total_not_reading = num_girls + num_boys - total_reading

    # return the result
    result = total_not_reading
    return result

print(solution())