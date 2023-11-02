def solution():
    """Mr. Bodhi is transporting some animals using a yacht across a river. He has 20 cows, 15 foxes and three times as many zebras as foxes.
    To balance the yacht to ensure a smooth sail across the river, the total number of animals in the yacht needs to be 100.
    If he decides to add sheep to the yacht to make the yacht sail-worthy, how many sheep did he add to the yacht?"""
    cows = 20
    foxes = 15
    zebras = 3 * foxes
    total_animals = cows + foxes + zebras
    sheep_needed = 100 - total_animals
    result = sheep_needed
    return result

print(solution())