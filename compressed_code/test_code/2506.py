def solution():
    
    total_chickens = 9000
    rooster_ratio = 2
    hen_ratio = 1
    total_ratio = rooster_ratio + hen_ratio
    rooster_fraction = rooster_ratio / total_ratio
    rooster_count = rooster_fraction * total_chickens
    result = rooster_count
    return result

print(solution())