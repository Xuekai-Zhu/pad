def solution():
    num_girls = 12
    num_boys = 10

    # Calculate the number of girls who are reading
    num_girls_reading = (5 / 6) * num_girls

    # Calculate the number of boys who are reading
    num_boys_reading = (4 / 5) * num_boys

    # Calculate the total number of students who are reading
    total_reading = num_girls_reading + num_boys_reading

    # Calculate the total number of students who are not reading
    total_not_reading = (num_girls + num_boys) - total_reading
    result = total_not_reading
    return result

print(solution())