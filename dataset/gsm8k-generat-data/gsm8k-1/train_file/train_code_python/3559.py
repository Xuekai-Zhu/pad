def solution():
    """Anna wants to grow some lettuce in the garden and would like to grow enough to have at least 12 large salads. She estimates that, despite her best efforts, half of the lettuce will be lost to insects and rabbits. Each lettuce plant is estimated to provide 3 large salads. How many lettuce plants should Anna grow in the garden?"""
    salads_needed = 12
    lettuce_per_salad = 0.5
    lettuce_per_plant = 3
    plants_needed = int(salads_needed / lettuce_per_salad / lettuce_per_plant) + 1
    result = plants_needed
    return result

print(solution())