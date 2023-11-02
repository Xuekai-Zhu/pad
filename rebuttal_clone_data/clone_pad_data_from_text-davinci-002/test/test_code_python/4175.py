def solution():
     total_students = 45
     proportion_under_11 = 1/3
     proportion_under_13 = 2/5
     students_under_11 = total_students * proportion_under_11
     students_under_13 = total_students * proportion_under_13
     students_13_and_over = total_students - students_under_11 - students_under_13
     result = students_13_and_over
     
     return result

print(solution())