def solution():
     total_students = 30
     total_boys = 10
     total_girls = total_students - total_boys
     cups_per_boy = 5
     total_cups = 90
     cups_per_girl = (total_cups - (total_boys * cups_per_boy)) / total_girls
     result = cups_per_girl
     return result

print(solution())