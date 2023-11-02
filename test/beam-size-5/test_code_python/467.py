def solution():
    
    num_students = 30
    pencils_per_student = 10
    total_pencils = num_students * pencils_per_student
    used_pencils = total_pencils * (1/5)
    remaining_pencils = total_pencils - used_pencils
    end_of_year_pencils = remaining_pencils * (1/3)
    pencils_left = remaining_pencils - end_of_year_pencils
    result = pencils_left
    return result

print(solution())