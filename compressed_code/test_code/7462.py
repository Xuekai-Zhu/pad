def solution():
    
    num_students = 12
    total_oranges = 108
    bad_oranges = 36
    good_oranges = total_oranges - bad_oranges
    oranges_per_student_without_waste = total_oranges // num_students
    oranges_per_student_with_waste = good_oranges // num_students
    difference = oranges_per_student_without_waste - oranges_per_student_with_waste
    result = difference
    return result

print(solution())