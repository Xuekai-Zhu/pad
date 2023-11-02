def solution():
    
    total_animals = 200
    num_cows = 40
    num_sheep = 56
    num_goats = total_animals - num_cows - num_sheep
    result = num_goats
    return result

print(solution())