def solution():
    squirrels_first_student = 12  # First student counted 12 squirrels
    squirrels_second_student = squirrels_first_student * (1 + 1/3)  # Second student counted a third more than the first
    total_squirrels = squirrels_first_student + squirrels_second_student
    result = total_squirrels
    return result

print(solution())