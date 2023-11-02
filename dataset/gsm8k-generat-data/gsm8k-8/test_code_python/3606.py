def solution():
    # Calculate the number of girls and boys in the school
    total_students = 800
    girls_fraction = 5/8
    girls_count = girls_fraction * total_students
    boys_count = total_students - girls_count

    # Calculate the number of girls and boys in the primary grades
    girls_prim = 7/10 * girls_count
    boys_prim = 2/5 * boys_count
    total_prim = girls_prim + boys_prim

    # Calculate the number of middle schoolers
    middle_schoolers = total_students - total_prim
    result = middle_schoolers
    return result

print(solution())