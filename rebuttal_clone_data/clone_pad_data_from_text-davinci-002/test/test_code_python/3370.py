def solution():
     folding_time = 4 * 5
     resting_time = 4 * 75
     mixing_time = 10
     baking_time = 30
     total_time = folding_time + resting_time + mixing_time + baking_time
     hours = total_time // 60
     result = hours
     return result

print(solution())