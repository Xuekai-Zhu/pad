def solution():
    # Calculate the total number of lettuce plants needed to grow at least 12 large salads
    salads_needed = 12  # total number of large salads needed
    lettuce_per_salad = 3  # number of large salads per lettuce plant
    lettuce_needed = salads_needed / lettuce_per_salad  # total number of lettuce plants needed, without accounting for loss
    lettuce_with_loss = lettuce_needed * 2  # total number of lettuce plants needed, accounting for 50% loss to insects and rabbits
    result = lettuce_with_loss
    return result

print(solution())