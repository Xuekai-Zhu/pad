def solution():
    
    total_weight = 8 + (6 * 2) + (2 * 12)
    fish_per_person = 2
    total_campers = total_weight // fish_per_person
    result = total_campers
    return result

print(solution())