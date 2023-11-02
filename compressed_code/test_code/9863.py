def solution():
    
    flowering_plants = 7
    fruiting_plants = 2 * flowering_plants
    new_flowering_plants = 3
    new_fruiting_plants = 2
    given_flowering_plants = 1
    given_fruiting_plants = 4
    remaining_flowering_plants = flowering_plants + new_flowering_plants - given_flowering_plants
    remaining_fruiting_plants = fruiting_plants + new_fruiting_plants - given_fruiting_plants
    result = remaining_flowering_plants + remaining_fruiting_plants
    return result

print(solution())