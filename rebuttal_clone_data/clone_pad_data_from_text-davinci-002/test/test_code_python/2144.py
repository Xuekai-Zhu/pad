def solution():
    Safari_lions = 100
    Safari_snakes = Safari_lions / 2
    Safari_giraffes = Safari_snakes - 10
    Savanna_lions = Safari_lions * 2
    Savanna_snakes = Safari_snakes * 3
    Savanna_giraffes = Safari_giraffes + 20
    result = Savanna_lions + Savanna_snakes + Savanna_giraffes
    return result

print(solution())