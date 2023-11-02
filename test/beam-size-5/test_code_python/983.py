def solution():
    
    soil_weight = 30
    rose_weight = 1
    carnation_weight = 1.5
    sunflowers = 4
    carnations = 10
    sunflower_weight = 3
    carnation_weight = 1
    total_weight = (sunflowers * sunflower_weight) + (carnations * carnation_weight)
    roses = soil_weight // rose_weight
    result = roses
    return result

print(solution())