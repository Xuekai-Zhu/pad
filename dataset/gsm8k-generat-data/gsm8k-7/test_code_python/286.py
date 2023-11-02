def solution():
    total_students = 18
    boys = 8
    girls = total_students - boys
    # Number of students present for the field trip was the same
    present_students = boys + girls

    # Calculate the number of girls who did not join the field trip
    girls_not_present = present_students - girls
    result = girls_not_present
    return result

print(solution())