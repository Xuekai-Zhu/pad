def solution():
     total_distance = 50
     first_day_distance = 10
     second_day_distance = total_distance / 2
     third_day_distance = total_distance - first_day_distance - second_day_distance
     result = third_day_distance
     return result

print(solution())