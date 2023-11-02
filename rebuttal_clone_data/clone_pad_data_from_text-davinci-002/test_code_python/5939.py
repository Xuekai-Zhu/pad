def solution():
     cans_collected_first_day = 20
     increase_per_day = 5
     days_collected_per_week = 5
     total_cans_collected_per_week = cans_collected_first_day + (increase_per_day * days_collected_per_week)
     result = total_cans_collected_per_week
     return result

print(solution())