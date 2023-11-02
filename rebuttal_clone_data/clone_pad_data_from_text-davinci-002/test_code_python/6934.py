def solution():
     morning_students = 25
     absent_morning = 3
     afternoon_students = 24
     absent_afternoon = 4
     
     total_students = morning_students - absent_morning + afternoon_students - absent_afternoon
     result = total_students
     return result

print(solution())