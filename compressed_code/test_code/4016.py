def solution():
    
    flowering_plants = 7
    fruiting_plants = 2 * flowering_plants
    saturday_plants = 3 + 2
    sunday_plants = 1 + 4
    total_plants = flowering_plants + fruiting_plants + saturday_plants - sunday_plants
    result = total_plants
    return result

print(solution())