def solution():
    
    jenny_red = 30
    jenny_blue = 25
    mary_red = 2 * jenny_red
    anie_red = mary_red + 20
    anie_blue = 2 * jenny_blue
    mary_blue = 0.5 * anie_blue
    total_blue = jenny_blue + mary_blue + anie_blue
    result = total_blue
    return result

print(solution())