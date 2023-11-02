def solution():
    pasture_size = 144
    num_sheep = 8
    num_cattle = 5
    grass_eaten_sheep = 1
    grass_eaten_cattle = 2
    corn_eaten_sheep = 2
    corn_eaten_cattle = 1
    cost_corn_bag = 10
    total_grass_sheep = num_sheep * 12 * grass_eaten_sheep
    total_grass_cattle = num_cattle * 12 * grass_eaten_cattle
    total_grass = total_grass_sheep + total_grass_cattle
    total_corn_sheep = num_sheep * 12 * corn_eaten_sheep
    total_corn_cattle = num_cattle * 12 * corn_eaten_cattle
    total_corn = total_corn_sheep + total_corn_cattle
    total_cost = (total_corn / corn_eaten_cattle) * cost_corn_bag
    result = total_cost
    return result

print(solution())