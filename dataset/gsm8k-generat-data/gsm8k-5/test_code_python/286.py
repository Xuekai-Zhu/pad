def solution():
    total_students = 18  # There were 18 students assigned for the field trip
    boys = 8  # There were 8 boys in the total count

    # Calculate the number of girls assigned for the field trip
    girls = total_students - boys

    # Calculate the number of girls who were not able to join the field trip
    missing_girls = girls - boys

    result = missing_girls
    return result

print(solution())