def solution():
    
    first_student_squirrels = 12
    second_student_squirrels = first_student_squirrels + (1/3 * first_student_squirrels)
    total_squirrels = first_student_squirrels + second_student_squirrels
    result = total_squirrels
    return result

print(solution())