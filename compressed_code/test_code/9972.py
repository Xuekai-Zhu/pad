def solution():
    
    shirts_per_hour = 4
    pants_per_hour = 3
    hours_shirts = 3
    hours_pants = 5
    total_shirts = shirts_per_hour * hours_shirts
    total_pants = pants_per_hour * hours_pants
    total_clothing = total_shirts + total_pants
    result = total_clothing
    return result

print(solution())