def solution():
    
    january_animals = 26
    february_animals = 3 * january_animals
    march_animals = february_animals / 2
    total_animals = january_animals + february_animals + march_animals
    result = total_animals
    return result

print(solution())