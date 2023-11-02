def solution():
     hours_worked = 4
     dollars_earned = 28
     dollars_desired = 70
     hours_needed = (dollars_desired - dollars_earned) / dollars_earned
     result = hours_needed
     return result

print(solution())