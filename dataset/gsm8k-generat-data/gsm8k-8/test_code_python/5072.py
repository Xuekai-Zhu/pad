def solution():
    total_butterflies = 9
    
    # Calculate the number of butterflies that fly away
    butterflies_fly_away = total_butterflies / 3
    
    # Calculate the number of butterflies left
    butterflies_left = total_butterflies - butterflies_fly_away
    
    result = butterflies_left
    return result

print(solution())