def solution():
    """The farm has 30 cows and the zoo has 20 sheep. The zoo has twice as many cows as the farm does. The farm has half as many sheep as the zoo does. How many animals do the farm and zoo have combined?"""
    farm_cows = 30
    zoo_sheep = 20
    zoo_cows = 2 * farm_cows
    farm_sheep = zoo_sheep / 2
    total_animals = farm_cows + zoo_cows + farm_sheep + zoo_sheep
    result = total_animals
    return result

print(solution())