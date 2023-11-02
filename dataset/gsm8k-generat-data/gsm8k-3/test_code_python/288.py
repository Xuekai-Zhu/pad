def solution():
    """There were 18 students assigned in a minibus for a field trip. Eight of these students were boys. On the day of the field trip, the number of girls and boys was the same since some of the girls were not able to join the trip. How many girls were not able to join the field trip?"""
    # Define the number of students and boys
    total_students = 18
    boys = 8

    # Calculate the number of girls
    girls = total_students - boys

    # Calculate the number of girls who were not able to join the field trip
    girls_not_able = abs(boys - girls) / 2

    # Display the number of girls who were not able to join the field trip
    result = girls_not_able
    return result

print(solution())