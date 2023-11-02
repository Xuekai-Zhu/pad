def solution():
    # Define the number of mangoes harvested
    mangoes_harvested = 560

    # Calculate the number of mangoes sold at the market
    mangoes_sold = mangoes_harvested / 2

    # Calculate the number of mangoes left
    mangoes_left = mangoes_harvested - mangoes_sold

    # Calculate the number of mangoes each neighbor receives
    mangoes_each_neighbor = mangoes_left / 8

    result = mangoes_each_neighbor
    return result

print(solution())