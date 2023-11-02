def solution():
     total_students = 100
     boy_ratio = 3
     girl_ratio = 2
     boys = total_students / boy_ratio
     girls = total_students / girl_ratio
     boy_girl_difference = boys - girls
     result = boy_girl_difference
     return result

print(solution())