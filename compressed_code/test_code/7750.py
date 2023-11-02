def solution():
    
    mangoes_harvested = 560
    mangoes_sold = mangoes_harvested / 2
    mangoes_left = mangoes_harvested - mangoes_sold
    neighbors = 8
    mangoes_per_neighbor = mangoes_left / neighbors
    result = mangoes_per_neighbor
    return result

print(solution())