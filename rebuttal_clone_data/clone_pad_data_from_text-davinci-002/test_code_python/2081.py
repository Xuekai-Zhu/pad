def solution():
     original_days_grounded = 14
     extra_days_grounded = 3
     grades_below_B = 4
     total_days_grounded = original_days_grounded + (extra_days_grounded * grades_below_B)
     result = total_days_grounded
     return result

print(solution())