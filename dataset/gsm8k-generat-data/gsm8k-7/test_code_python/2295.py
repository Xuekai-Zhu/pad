def solution():
    total_students = 123
    single_students = 3

    # Calculate the number of couples who attended
    num_couples = (total_students - single_students) // 2
    result = num_couples
    return result

print(solution())