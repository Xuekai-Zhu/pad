def solution():
    # Define the number of girls and boys in the class
    num_girls = 12
    num_boys = 10

    # Calculate the number of girls and boys who are reading
    girls_reading = int(5/6 * num_girls)
    boys_reading = int(4/5 * num_boys)

    # Calculate the total number of students who are reading
    total_reading = girls_reading + boys_reading

    # Calculate the number of students who are not reading
    not_reading = (num_girls + num_boys) - total_reading
    result = not_reading
    return result

print(solution())