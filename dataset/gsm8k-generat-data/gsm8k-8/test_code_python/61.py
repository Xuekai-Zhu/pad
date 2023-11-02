def solution():
    # Define the total weight the bear needs to gain
    total_weight = 1000

    # Calculate how much the bear gained from berries
    berries_weight = total_weight / 5

    # Calculate how much the bear gained from acorns
    acorns_weight = 2 * berries_weight

    # Calculate how much weight the bear gained from salmon
    salmon_weight = (total_weight - berries_weight - acorns_weight) / 2

    # Calculate how much weight the bear gained from small woodland animals
    small_animals_weight = total_weight - berries_weight - acorns_weight - salmon_weight

    result = small_animals_weight
    return result

print(solution())