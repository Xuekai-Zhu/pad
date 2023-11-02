def solution():
    num_students = 800
    num_girls = num_students * 5/8
    num_boys = num_students - num_girls

    # Calculate the number of girls in primary grades
    num_primary_girls = num_girls * 7/10

    # Calculate the number of boys in primary grades
    num_primary_boys = num_boys * 2/5

    # Calculate the total number of primary students
    num_primary_students = num_primary_girls + num_primary_boys

    # Calculate the number of middle schoolers
    num_middle_schoolers = num_students - num_primary_students
    result = num_middle_schoolers
    return result

print(solution())