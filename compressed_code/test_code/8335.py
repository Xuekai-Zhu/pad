def solution():
    
    total_chickens = 9000
    rooster_to_hen_ratio = 2/1
    roosters = total_chickens / (rooster_to_hen_ratio + 1) * rooster_to_hen_ratio
    result = roosters
    return result

print(solution())