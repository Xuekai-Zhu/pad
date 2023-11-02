def solution():
    # Number of girls and boys in the class
    girls = 12
    boys = 10

    # Calculate the number of girls and boys who are reading
    girls_reading = int(5 / 6 * girls)
    boys_reading = int(4 / 5 * boys)

    # Calculate the number of girls and boys who are not reading
    girls_not_reading = girls - girls_reading
    boys_not_reading = boys - boys_reading

    # Calculate the total number of students who are not reading
    total_not_reading = girls_not_reading + boys_not_reading
    result = total_not_reading
    return result

print(solution())