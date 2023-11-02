def solution():
    total_students = 5 * 28  # There are 5 vans, each carrying 28 students
    boys = 60  # Out of these students, 60 are boys

    # Calculate the number of girls
    girls = total_students - boys
    result = girls
    return result

print(solution())