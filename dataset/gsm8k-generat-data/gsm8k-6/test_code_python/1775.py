def solution():
    # Calculate the number of squirrels counted by the first student
    squirrels_1 = 12
    # Calculate the number of squirrels counted by the second student, which is a third more than the first
    squirrels_2 = squirrels_1 + (squirrels_1 * 1/3)
    # Calculate the total number of squirrels counted by both students
    total_squirrels = squirrels_1 + squirrels_2
    result = total_squirrels
    return result

print(solution())