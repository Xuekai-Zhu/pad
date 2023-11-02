def solution():
    """Mr. Bodhi is transporting some animals using a yacht across a river. He has 20 cows, 15 foxes and three times as many zebras as foxes. To balance the yacht to ensure a smooth sail across the river, the total number of animals in the yacht needs to be 100. If he decides to add sheep to the yacht to make the yacht sail-worthy, how many sheep did he add to the yacht?"""
    # Define the number of cows, foxes, and zebras
    cows = 20
    foxes = 15
    zebras = 3 * foxes

    # Calculate the total number of animals
    total_animals = cows + foxes + zebras

    # Calculate the number of sheep needed to balance the yacht
    sheep = 100 - total_animals

    # return the result
    result = sheep
    return result

print(solution())