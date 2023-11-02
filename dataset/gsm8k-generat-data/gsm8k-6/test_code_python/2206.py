def solution():
    # Calculate the number of plants that survived
    tomatoes_survived = 6 / 2
    peppers_survived = 4 - 1  # one pepper plant died

    # Calculate the total number of vegetables harvested
    veg_from_tomatoes = tomatoes_survived * 7
    veg_from_eggplants = 2 * 7
    veg_from_peppers = peppers_survived * 7
    total_veg = veg_from_tomatoes + veg_from_eggplants + veg_from_peppers
    result = total_veg
    return result

print(solution())