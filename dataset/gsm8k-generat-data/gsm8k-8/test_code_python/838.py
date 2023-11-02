def solution():
    # Define the initial number of animals
    sheep = 20
    cows = 10
    dogs = 14

    # Subtract the animals that drowned
    sheep -= 3
    cows -= 6
    total_animals = sheep + cows + dogs

    result = total_animals
    return result

print(solution())