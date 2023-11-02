def solution():
    """There were 18 students assigned in a minibus for a field trip. Eight of these students were boys. On the day of the field trip, the number of girls and boys was the same since some of the girls were not able to join the trip. How many girls were not able to join the field trip?"""
    # Define the number of boys
    boys = 8

    # Define the total number of students
    total_students = 18

    # Calculate the number of girls
    girls = total_students - boys

    # Calculate the number of students who went on the field trip
    students_on_trip = boys + girls

    # Calculate the number of girls who did not join the field trip
    girls_not_on_trip = girls - (students_on_trip / 2)

    # return the result
    result = girls_not_on_trip
    return result

print(solution())