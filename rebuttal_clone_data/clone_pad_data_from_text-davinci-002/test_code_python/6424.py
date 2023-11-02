def solution():
     total_students = 32
     a_students = total_students * 0.25
     b_c_students = total_students * 0.25 - a_students
     failed_students = total_students - a_students - b_c_students
     result = failed_students 
     return result

print(solution())