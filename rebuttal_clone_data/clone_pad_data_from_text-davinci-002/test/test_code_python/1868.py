def solution():
     total_days = 180
     allowable_absences = total_days * 0.05
     used_absences = 6
     remaining_absences = allowable_absences - used_absences
     result = remaining_absences
     return result

print(solution())