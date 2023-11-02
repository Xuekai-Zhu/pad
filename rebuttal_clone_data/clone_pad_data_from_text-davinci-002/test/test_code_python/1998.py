def solution():
    desired_salads = 12
    estimated_loss = 0.5
    salads_per_plant = 3
    number_of_plants = (desired_salads / (1 - estimated_loss)) / salads_per_plant
    result = number_of_plants
    return result

print(solution())