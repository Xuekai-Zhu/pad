def solution():
    
    cows = 20
    ducks = cows * 1.5
    total_animals = cows + ducks + (cows + ducks) / 5
    result = total_animals
    return result

print(solution())