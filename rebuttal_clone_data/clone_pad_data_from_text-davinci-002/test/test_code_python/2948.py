def solution():
    flowering_plants = 7
    fruiting_plants = 2 * flowering_plants
    plants_bought = 3 + 2
    plants_given_away = 1 + 4
    remaining_plants = flowering_plants + fruiting_plants - plants_bought + plants_given_away
    result = remaining_plants
    return result

print(solution())