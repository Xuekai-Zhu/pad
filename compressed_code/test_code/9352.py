def solution():
    
    
    cows = 40
    cow_water = 80
    sheep = 10 * cows
    sheep_water = cow_water / 4
    total_water = (cows * cow_water + sheep * sheep_water) * 7
    
    return total_water

print(solution())