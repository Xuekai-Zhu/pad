def solution():
     total_students = 50
     starting_students = 40
     increment = 10
     total_years = 10
     final_student_count = starting_students + (total_students * total_years) - (increment * total_years)
     result = final_student_count
     return result

print(solution())