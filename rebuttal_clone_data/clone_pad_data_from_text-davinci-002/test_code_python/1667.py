def solution():
     streets_patrolled_by_officer_A = 36
     streets_patrolled_by_officer_B = 55
     hours_patrolled_by_officer_A = 4
     hours_patrolled_by_officer_B = 5
     streets_patrolled_in_one_hour = (streets_patrolled_by_officer_A + streets_patrolled_by_officer_B) / (hours_patrolled_by_officer_A + hours_patrolled_by_officer_B)
     result = streets_patrolled_in_one_hour
     return result

print(solution())