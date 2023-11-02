def solution():
    
    safari_lions = 100
    safari_snakes = safari_lions / 2
    safari_giraffes = safari_snakes - 10
    savanna_lions = 2 * safari_lions
    savanna_snakes = 3 * safari_snakes
    savanna_giraffes = safari_giraffes + 20
    total_animals = savanna_lions + savanna_snakes + savanna_giraffes
    result = total_animals
    return result

print(solution())