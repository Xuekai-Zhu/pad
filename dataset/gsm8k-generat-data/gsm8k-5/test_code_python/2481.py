def solution():
    mangoes_harvested = 560  # Mr. Wong harvested 560 mangoes
    mangoes_sold = mangoes_harvested / 2  # Mr. Wong sold half of the mangoes
    mangoes_left = mangoes_harvested - mangoes_sold  # Mr. Wong has mangoes left to distribute

    # Calculate the number of mangoes each neighbor gets
    mangoes_per_neighbor = mangoes_left / 8
    result = mangoes_per_neighbor
    return result

print(solution())