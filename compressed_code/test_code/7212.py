def solution():
    
    jenny_red = 30
    jenny_blue = 25
    mary_red = jenny_red * 2
    anie_red = mary_red + 20
    anie_blue = jenny_blue * 2
    mary_blue = anie_blue / 2
    
    total_blue = jenny_blue + mary_blue + anie_blue
    result = total_blue
    
    return result

print(solution())