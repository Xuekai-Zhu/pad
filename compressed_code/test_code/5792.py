def solution():
    
    pink_hats = 26
    green_hats = 15
    yellow_hats = 24

    
    pink_hats = pink_hats - 4

    
    pink_removed = 6
    green_removed = pink_removed * 2
    pink_hats = pink_hats - pink_removed
    green_hats = green_hats - green_removed

    
    total_hats = pink_hats + green_hats + yellow_hats
    result = total_hats

    return result

print(solution())