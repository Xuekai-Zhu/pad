def solution():
    num_students = 39
    fraction_participated = 1/3

    # Calculate the number of students who participated
    num_participated = num_students * fraction_participated

    # Calculate the number of students who did not participate
    num_not_participated = num_students - num_participated
    result = num_not_participated
    return result

print(solution())