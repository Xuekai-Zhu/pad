def solution():
    
    cows = 20
    ducks = cows * 1.5
    total_animals = cows + ducks
    pigs = total_animals / 5
    total_animals += pigs
    result = total_animals
    return result

print(solution())