def solution():
    num_salads_needed = 12
    lettuce_loss = 0.5  # 50% loss
    salads_per_plant = 3

    # Calculate the total number of salads needed, accounting for loss
    total_salads_needed = num_salads_needed / (1 - lettuce_loss)

    # Calculate the minimum number of lettuce plants needed to provide the total salads
    num_plants_needed = total_salads_needed / salads_per_plant
    result = num_plants_needed
    return result

print(solution())