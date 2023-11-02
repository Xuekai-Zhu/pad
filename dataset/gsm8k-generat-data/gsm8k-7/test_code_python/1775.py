def solution():
    squirrels_first_student = 12
    squirrels_second_student = squirrels_first_student + (squirrels_first_student / 3)

    total_squirrels = squirrels_first_student + squirrels_second_student
    result = total_squirrels
    return result

print(solution())