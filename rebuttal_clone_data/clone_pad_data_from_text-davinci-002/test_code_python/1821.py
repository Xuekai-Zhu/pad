def solution():
     total_students = 24
     students_before_lunch = total_students // 3
     students_after_lunch = 10
     students_after_gym = total_students - students_before_lunch - students_after_lunch
     result = students_after_gym
     
     return result

print(solution())