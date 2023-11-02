def solution():
    # Define the number of boys in the minibus
    boys = 8

    # Calculate the total number of students on the day of the field trip
    total_students = 18 - (8 - boys)

    # Calculate the number of girls on the day of the field trip
    girls = total_students - boys

    # Calculate the number of girls who were not able to join the field trip
    girls_not_able = girls - boys

    result = girls_not_able
    return result

print(solution())