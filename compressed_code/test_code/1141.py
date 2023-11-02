def solution():
    
    hunting_per_month = 6
    hunting_season = 0.25  
    deers_caught_per_hunting = 2
    deer_weight = 600
    total_deer_caught = hunting_per_month * 12 * hunting_season * deers_caught_per_hunting
    total_weight = total_deer_caught * deer_weight
    weight_kept = total_weight / 2
    result = weight_kept
    return result

print(solution())