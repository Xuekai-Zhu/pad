def solution():
    # Calculate the total weight of each type of instrument
    trumpets_weight = 5 * 6
    clarinets_weight = 5 * 9
    trombones_weight = 10 * 8
    tubas_weight = 20 * 3
    drums_weight = 15 * 2

    # Calculate the total weight of the marching band
    total_weight = trumpets_weight + clarinets_weight + trombones_weight + tubas_weight + drums_weight
    result = total_weight
    return result

print(solution())