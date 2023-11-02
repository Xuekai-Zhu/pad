def solution():
     cans_collected_week_1 = 158
     cans_collected_week_2 = 259
     total_cans_needed = 500
     cans_left_to_collect = total_cans_needed - (cans_collected_week_1 + cans_collected_week_2)
     result = cans_left_to_collect
     return result

print(solution())