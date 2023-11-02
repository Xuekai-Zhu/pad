def solution():
     initial_students = 200
     percent_increase = 50
     current_year = 3
     total_students = initial_students * (1 + (percent_increase / 100)) ** current_year
     result = total_students
     return result

print(solution())