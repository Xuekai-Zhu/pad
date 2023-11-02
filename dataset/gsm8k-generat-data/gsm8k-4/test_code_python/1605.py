def solution():
    """There are 92 students altogether. Twenty of them ride the school bus home together, 5/8 of the remaining ride their own bike home, and the rest whose houses are near the school walk home. How many students are walking home?"""
    # Define the total number of students
    total_students = 92

    # Calculate the number of students on the school bus
    bus_students = 20

    # Calculate the number of remaining students
    remaining_students = total_students - bus_students

    # Calculate the number of students riding their bikes
    bike_students = remaining_students * 5/8

    # Calculate the number of students walking home
    walking_students = total_students - bus_students - bike_students

    # return the result
    result = walking_students
    return result

print(solution())