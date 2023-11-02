def solution():
    
    total_plants = 30
    eaten_plants = 20
    remaining_plants = total_plants - eaten_plants
    half_remaining_plants = remaining_plants / 2
    final_plants = half_remaining_plants - 1
    result = final_plants
    return result

print(solution())