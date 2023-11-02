def solution():
     apples_packed_per_day = 40
     boxes_per_day = 50
     apples_packed_per_week = apples_packed_per_day * boxes_per_day
     apples_packed_per_day_2 = apples_packed_per_day - 10
     boxes_per_day_2 = 50
     apples_packed_per_week_2 = apples_packed_per_day_2 * boxes_per_day_2
     total_apples_packed = apples_packed_per_week + apples_packed_per_week_2
     result = total_apples_packed
     return result

print(solution())