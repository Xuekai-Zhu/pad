def solution():
     initial_weight = 120
     muscle_weight = initial_weight * 0.2
     fat_weight = muscle_weight / 4
     total_weight = initial_weight + muscle_weight + fat_weight
     result = total_weight
     return result

print(solution())