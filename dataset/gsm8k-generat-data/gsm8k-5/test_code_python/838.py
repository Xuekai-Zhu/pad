def solution():
    # Initial animal counts
    sheep = 20
    cows = 10
    dogs = 14

    # Animal counts after the accident
    sheep -= 3  # 3 sheep drowned
    cows -= 6  # Twice as many cows as sheep drowned
    dogs += 0  # All of the dogs made it to shore

    # Total number of animals that made it to shore
    total_animals = sheep + cows + dogs
    result = total_animals
    return result

print(solution())