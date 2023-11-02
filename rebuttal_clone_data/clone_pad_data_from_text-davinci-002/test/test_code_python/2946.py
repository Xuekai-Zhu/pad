def solution():
     total_students = 325
     students_with_glasses = total_students * (40 / 100)
     students_without_glasses = total_students - students_with_glasses
     result = students_without_glasses
     
     return result

print(solution())